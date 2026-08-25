"""Kotlin Idiomatic and Multiplatform pattern detection rules."""

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


class ExtensionFunctionAdapterRule(BaseRule):
    """Detects Kotlin Extension Functions and Properties providing retroactive API adaptation."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.extensions:
            score = 0.90
            evidences = [
                Evidence(
                    rule_code="KOTLIN_EXTENSION_FUNCTION",
                    description=f"Extension function '{fn.receiver_type}.{fn.name}' retroactively augments type without subclassing",
                    weight=score,
                    location=fn.location,
                )
            ]
            detections.append(
                Detection(
                    pattern_type=PatternType.EXTENSION_FUNCTION_ADAPTER,
                    pattern_category=PatternCategory.KOTLIN_IDIOMATIC,
                    target_name=f"{fn.receiver_type}.{fn.name}",
                    target_kind="extension_function",
                    confidence=Confidence(score=score, evidences=evidences),
                    primary_location=fn.location,
                    evidences=evidences,
                )
            )
        return detections


class DelegatedPropertyLazyRule(BaseRule):
    """Detects Delegated Properties (`by lazy`, `by Delegates.observable`, `by viewModels()`, custom delegate)."""

    DELEGATE_KEYWORD = re.compile(r"\bby\s+(lazy|Delegates\.\w+|viewModels|activityViewModels|inject|rememberSaveable|\w+Delegate)")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for prop in model.all_properties:
            if prop.is_delegated or prop.is_lazy or self.DELEGATE_KEYWORD.search(prop.raw_text or ""):
                delegate_kind = prop.delegate_expression or "lazy/custom"
                evidences = [
                    Evidence(
                        rule_code="KOTLIN_DELEGATED_PROPERTY",
                        description=f"Property '{prop.name}' delegates accessor behavior via '{delegate_kind}'",
                        weight=0.90,
                        location=prop.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.DELEGATED_PROPERTY_LAZY,
                        pattern_category=PatternCategory.KOTLIN_IDIOMATIC,
                        target_name=prop.name,
                        target_kind="property",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=prop.location,
                        evidences=evidences,
                    )
                )
        return detections


class SealedHierarchyAdtRule(BaseRule):
    """Detects Sealed Class / Interface Algebraic Data Types (ADTs) for exhaustive domain modeling."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.sealed_types:
            evidences = [
                Evidence(
                    rule_code="KOTLIN_SEALED_HIERARCHY",
                    description=f"Sealed type '{t.name}' ({t.kind}) defines an Algebraic Data Type (ADT) hierarchy for exhaustive pattern matching",
                    weight=0.95,
                    location=t.location,
                )
            ]
            detections.append(
                Detection(
                    pattern_type=PatternType.SEALED_HIERARCHY_ADT,
                    pattern_category=PatternCategory.KOTLIN_IDIOMATIC,
                    target_name=t.name,
                    target_kind=t.kind,
                    confidence=Confidence(score=0.95, evidences=evidences),
                    primary_location=t.location,
                    evidences=evidences,
                )
            )
        return detections


class InlineValueClassRule(BaseRule):
    """Detects `@JvmInline value class` domain primitives preventing primitive obsession."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_types:
            if t.is_value or "value_class" in t.kind or any("@JvmInline" in a for a in t.annotations):
                evidences = [
                    Evidence(
                        rule_code="KOTLIN_INLINE_VALUE_CLASS",
                        description=f"Value class '{t.name}' encapsulates strongly typed domain primitive with zero runtime allocation overhead",
                        weight=0.95,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.INLINE_VALUE_CLASS,
                        pattern_category=PatternCategory.KOTLIN_IDIOMATIC,
                        target_name=t.name,
                        target_kind="value_class",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class CompanionStaticFactoryRule(BaseRule):
    """Detects Companion Object factories (`create()`, `of()`, `operator fun invoke`)."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_types:
            for comp in t.companion_objects:
                factory_methods = [
                    fn for fn in comp.functions
                    if fn.name in ("create", "of", "from", "invoke", "newInstance") or fn.is_operator
                ]
                if factory_methods or "Factory" in comp.name:
                    evidences = [
                        Evidence(
                            rule_code="KOTLIN_COMPANION_FACTORY",
                            description=f"Companion object on '{t.name}' encapsulates static creation factory method(s): {', '.join(f.name for f in factory_methods[:2])}",
                            weight=0.85,
                            location=comp.location or t.location,
                        )
                    ]
                    detections.append(
                        Detection(
                            pattern_type=PatternType.COMPANION_STATIC_FACTORY,
                            pattern_category=PatternCategory.KOTLIN_IDIOMATIC,
                            target_name=f"{t.name}.Companion",
                            target_kind="companion_object",
                            confidence=Confidence(score=0.85, evidences=evidences),
                            primary_location=comp.location or t.location,
                            evidences=evidences,
                        )
                    )
        return detections


class OperatorOverloadingDslRule(BaseRule):
    """Detects custom `operator fun` implementations."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if fn.is_operator or "operator fun" in fn.raw_text:
                evidences = [
                    Evidence(
                        rule_code="KOTLIN_OPERATOR_OVERLOADING",
                        description=f"Operator function '{fn.name}' overloads language operators for domain expression semantics",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.OPERATOR_OVERLOADING_DSL,
                        pattern_category=PatternCategory.KOTLIN_IDIOMATIC,
                        target_name=fn.name,
                        target_kind="operator_function",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class ScopeFunctionChainRule(BaseRule):
    """Detects idiomatic Kotlin scope function pipelines (`apply`, `also`, `let`, `run`, `with`)."""

    SCOPE_PIPELINE = re.compile(r"\.(apply|also|let|run)\s*\{")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            matches = self.SCOPE_PIPELINE.findall(fn.body or "")
            if len(matches) >= 2:
                evidences = [
                    Evidence(
                        rule_code="KOTLIN_SCOPE_FUNCTION_PIPELINE",
                        description=f"Function '{fn.name}' coordinates object lifecycle via {len(matches)} scope functions ({', '.join(matches[:3])})",
                        weight=0.80,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.SCOPE_FUNCTION_CHAIN,
                        pattern_category=PatternCategory.KOTLIN_IDIOMATIC,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.80, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections
