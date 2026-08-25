"""Resilience, Memory Safety & Hazard rules for Kotlin & Android."""

from __future__ import annotations

import re
from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BaseRule
from pattern_detector.domain.value_objects import (
    Confidence,
    Evidence,
    PatternCategory,
    PatternType,
    SourceLocation,
)


class GlobalScopeCoroutineLeakRule(BaseRule):
    """Detects unconfined coroutines launched via `GlobalScope` causing memory/job leaks."""

    GLOBALSCOPE_PATTERN = re.compile(r"\bGlobalScope\.(launch|async)\b")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if self.GLOBALSCOPE_PATTERN.search(fn.body or ""):
                evidences = [
                    Evidence(
                        rule_code="HAZARD_GLOBALSCOPE_LEAK",
                        description=f"Function '{fn.name}' launches unconfined coroutine in GlobalScope escaping lifecycle bounds",
                        weight=0.95,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.GLOBALSCOPE_COROUTINE_LEAK,
                        pattern_category=PatternCategory.RESILIENCE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class NonCancellationExceptionSwallowRule(BaseRule):
    """Detects generic exception swallowing in coroutines without rethrowing CancellationException."""

    SWALLOW_PATTERN = re.compile(r"catch\s*\(\s*\w+\s*:\s*(?:Exception|Throwable)\s*\)\s*\{(?![^}]*\bthrow\b)")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if fn.is_suspend and self.SWALLOW_PATTERN.search(fn.body or ""):
                evidences = [
                    Evidence(
                        rule_code="HAZARD_CANCELLATION_EXCEPTION_SWALLOWED",
                        description=f"Suspending function '{fn.name}' catches generic Exception without rethrowing CancellationException, breaking coroutine cancellation",
                        weight=0.88,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.NON_CANCELLATION_EXCEPTION_SWALLOW,
                        pattern_category=PatternCategory.RESILIENCE,
                        target_name=fn.name,
                        target_kind="suspend_function",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class ForceNullAssertionHazardRule(BaseRule):
    """Detects unsafe force-null assertions (`!!`) risking runtime NullPointerException."""

    DOUBLE_BANG_PATTERN = re.compile(r"(\w+!!|\)!!)")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for f in model.files:
            occurrences: list[tuple[int, str]] = []
            for line_idx, line in enumerate(f.lines, 1):
                trimmed = line.strip()
                if trimmed.startswith("//") or trimmed.startswith("/*") or trimmed.startswith("*"):
                    continue
                match = self.DOUBLE_BANG_PATTERN.search(trimmed)
                if match:
                    occurrences.append((line_idx, match.group(1)))

            if occurrences:
                loc = SourceLocation(file_path=f.file_path, line=occurrences[0][0], column=1)
                evidences = [
                    Evidence(
                        rule_code="HAZARD_FORCE_NULL_ASSERTION",
                        description=f"Unsafe force-null assertion ('{occurrences[0][1]}') risks NullPointerException at runtime",
                        weight=0.85,
                        location=loc,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.FORCE_NULL_ASSERTION_HAZARD,
                        pattern_category=PatternCategory.RESILIENCE,
                        target_name=occurrences[0][1],
                        target_kind="expression",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=loc,
                        related_locations=[SourceLocation(file_path=f.file_path, line=ln, column=1) for ln, _ in occurrences[1:]],
                        evidences=evidences,
                    )
                )
        return detections


class ForceCastHazardRule(BaseRule):
    """Detects unsafe force downcasting (`as ` instead of `as?`) risking ClassCastException."""

    UNSAFE_CAST_PATTERN = re.compile(r"\bas\s+(?![?])[A-Z]\w+")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            match = self.UNSAFE_CAST_PATTERN.search(fn.body or "")
            if match:
                evidences = [
                    Evidence(
                        rule_code="HAZARD_UNSAFE_FORCE_CAST",
                        description=f"Function '{fn.name}' performs unsafe downcast ('{match.group(0)}') without safe cast 'as?'",
                        weight=0.80,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.FORCE_CAST_HAZARD,
                        pattern_category=PatternCategory.RESILIENCE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.80, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class MainThreadBlockingCallRule(BaseRule):
    """Detects synchronous blocking operations (`Thread.sleep`, `runBlocking`) in UI/ViewModel contexts."""

    BLOCKING_PATTERN = re.compile(r"\b(Thread\.sleep|runBlocking)\s*\(")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            is_ui_scope = "ViewModel" in t.name or "Activity" in t.name or "Fragment" in t.name or "Composable" in t.raw_text
            for fn in t.functions:
                if (is_ui_scope or fn.is_suspend) and self.BLOCKING_PATTERN.search(fn.body or ""):
                    evidences = [
                        Evidence(
                            rule_code="HAZARD_MAIN_THREAD_BLOCKING",
                            description=f"Method '{t.name}.{fn.name}' executes synchronous blocking call on Main/UI context, risking ANR",
                            weight=0.90,
                            location=fn.location,
                        )
                    ]
                    detections.append(
                        Detection(
                            pattern_type=PatternType.MAIN_THREAD_BLOCKING_CALL,
                            pattern_category=PatternCategory.RESILIENCE,
                            target_name=f"{t.name}.{fn.name}",
                            target_kind="method",
                            confidence=Confidence(score=0.90, evidences=evidences),
                            primary_location=fn.location,
                            evidences=evidences,
                        )
                    )
        return detections


class StrongContextLeakRule(BaseRule):
    """Detects retention of Android Activity / Context references in static/companion objects."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_types:
            if t.is_companion or t.is_object:
                context_props = [
                    p for p in t.properties
                    if p.type_name in ("Context", "Activity", "Context?", "Activity?") and "WeakReference" not in p.type_name
                ]
                if context_props:
                    evidences = [
                        Evidence(
                            rule_code="HAZARD_STRONG_CONTEXT_LEAK",
                            description=f"Object '{t.name}' retains strong static reference to Android '{context_props[0].type_name}', causing activity memory leaks",
                            weight=0.95,
                            location=t.location,
                        )
                    ]
                    detections.append(
                        Detection(
                            pattern_type=PatternType.STRONG_CONTEXT_LEAK,
                            pattern_category=PatternCategory.RESILIENCE,
                            target_name=t.name,
                            target_kind="object",
                            confidence=Confidence(score=0.95, evidences=evidences),
                            primary_location=t.location,
                            evidences=evidences,
                        )
                    )
        return detections
