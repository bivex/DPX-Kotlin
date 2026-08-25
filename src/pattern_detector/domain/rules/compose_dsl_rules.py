"""Jetpack Compose & Type-Safe DSL rules for Kotlin."""

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
)


class TypeSafeBuilderDslRule(BaseRule):
    """Detects Type-Safe Builders and declarative DSLs using lambda with receiver (`T.() -> Unit`) and `@DslMarker`."""

    RECEIVER_LAMBDA_PATTERN = re.compile(r"[A-Za-z0-9_.]+\.\(\s*\)\s*->\s*(Unit|[A-Za-z0-9_]+)")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            has_receiver_param = any(self.RECEIVER_LAMBDA_PATTERN.search(p[1]) for p in fn.parameters)
            has_dsl_marker = any("@DslMarker" in a for a in fn.annotations)
            if has_receiver_param or has_dsl_marker or "Dsl" in fn.name:
                score = 0.95 if has_dsl_marker else 0.85
                evidences = [
                    Evidence(
                        rule_code="COMPOSE_TYPE_SAFE_BUILDER_DSL",
                        description=f"Function '{fn.name}' implements Type-Safe Builder DSL accepting higher-order lambda with receiver",
                        weight=score,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.TYPE_SAFE_BUILDER_DSL,
                        pattern_category=PatternCategory.COMPOSE_DSL,
                        target_name=fn.name,
                        target_kind="dsl_function",
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class ComposeDeclarativeViewRule(BaseRule):
    """Detects Jetpack Compose declarative UI components (`@Composable fun`)."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if any("@Composable" in a for a in fn.annotations) or "@Composable" in fn.raw_text:
                evidences = [
                    Evidence(
                        rule_code="COMPOSE_DECLARATIVE_VIEW",
                        description=f"Composable function '{fn.name}' acts as a declarative UI component",
                        weight=0.95,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.COMPOSE_DECLARATIVE_VIEW,
                        pattern_category=PatternCategory.COMPOSE_DSL,
                        target_name=fn.name,
                        target_kind="composable_view",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class RememberMutableStateRule(BaseRule):
    """Detects Compose observable state holding (`remember { mutableStateOf(...) }`)."""

    REMEMBER_PATTERN = re.compile(r"\bremember(?:\s*\{|\s*Saveable|\s*\(|\s*\{\s*mutableStateOf)")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if self.REMEMBER_PATTERN.search(fn.body or ""):
                evidences = [
                    Evidence(
                        rule_code="COMPOSE_REMEMBER_MUTABLE_STATE",
                        description=f"Function '{fn.name}' preserves observable UI state across recompositions using remember",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.REMEMBER_MUTABLE_STATE,
                        pattern_category=PatternCategory.COMPOSE_DSL,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class ViewModelStateHolderRule(BaseRule):
    """Detects Android Architecture Component `ViewModel` managing UI state across configuration changes."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            if "ViewModel" in t.inherited_types or t.name.endswith("ViewModel"):
                evidences = [
                    Evidence(
                        rule_code="COMPOSE_VIEWMODEL_STATE_HOLDER",
                        description=f"Class '{t.name}' implements ViewModel architectural state holder",
                        weight=0.95,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.VIEW_MODEL_STATE_HOLDER,
                        pattern_category=PatternCategory.COMPOSE_DSL,
                        target_name=t.name,
                        target_kind="class",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections
