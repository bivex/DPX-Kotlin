"""GoF Creational design pattern detection rules for Kotlin (5/5)."""

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


class SingletonObjectDeclarationRule(BaseRule):
    """Detects Kotlin `object` declarations acting as thread-safe, lazy Singletons."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.objects:
            if not t.is_companion:
                evidences = [
                    Evidence(
                        rule_code="CREATIONAL_SINGLETON_OBJECT",
                        description=f"Object declaration '{t.name}' provides language-level thread-safe Singleton",
                        weight=0.95,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.SINGLETON_OBJECT_DECLARATION,
                        pattern_category=PatternCategory.CREATIONAL,
                        target_name=t.name,
                        target_kind="object",
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class FactoryMethodRule(BaseRule):
    """Detects Factory Method pattern for instantiating polymorphic domain types."""

    FACTORY_NAME_PATTERN = re.compile(r"\b(create[A-Z]\w+|make[A-Z]\w+|build[A-Z]\w+|newInstance)\b")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_types:
            for fn in t.functions:
                if self.FACTORY_NAME_PATTERN.search(fn.name) or ("Factory" in t.name and fn.name.startswith("create")):
                    evidences = [
                        Evidence(
                            rule_code="CREATIONAL_FACTORY_METHOD",
                            description=f"Method '{fn.name}' on '{t.name}' encapsulates instance instantiation as a Factory Method",
                            weight=0.85,
                            location=fn.location,
                        )
                    ]
                    detections.append(
                        Detection(
                            pattern_type=PatternType.FACTORY_METHOD,
                            pattern_category=PatternCategory.CREATIONAL,
                            target_name=f"{t.name}.{fn.name}",
                            target_kind="function",
                            confidence=Confidence(score=0.85, evidences=evidences),
                            primary_location=fn.location,
                            evidences=evidences,
                        )
                    )
        return detections


class AbstractFactoryRule(BaseRule):
    """Detects Abstract Factory interfaces declaring families of creation methods."""

    FACTORY_NAME_PATTERN = re.compile(r"\b(create[A-Z]\w+|make[A-Z]\w+)\b")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for iface in model.interfaces:
            creation_methods = [fn for fn in iface.functions if self.FACTORY_NAME_PATTERN.search(fn.name)]
            if len(creation_methods) >= 2 or ("Factory" in iface.name and len(creation_methods) >= 1):
                score = 0.90 if len(creation_methods) >= 2 else 0.80
                evidences = [
                    Evidence(
                        rule_code="CREATIONAL_ABSTRACT_FACTORY",
                        description=f"Interface '{iface.name}' defines Abstract Factory contract declaring {len(creation_methods)} creation method(s)",
                        weight=score,
                        location=iface.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.ABSTRACT_FACTORY,
                        pattern_category=PatternCategory.CREATIONAL,
                        target_name=iface.name,
                        target_kind="interface",
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=iface.location,
                        evidences=evidences,
                    )
                )
        return detections


class BuilderFluentChainRule(BaseRule):
    """Detects Builder pattern via fluent method chaining returning `this` or Builder class."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            chain_methods = [
                fn for fn in t.functions
                if (fn.return_type == t.name or fn.return_type == "Builder") and (fn.name.startswith("set") or fn.name.startswith("with") or fn.name.startswith("add"))
            ]
            if len(chain_methods) >= 2 or "Builder" in t.name:
                score = 0.90 if "Builder" in t.name else 0.80
                evidences = [
                    Evidence(
                        rule_code="CREATIONAL_BUILDER_FLUENT_CHAIN",
                        description=f"Class '{t.name}' implements fluent Builder pattern chaining {len(chain_methods)} configuration step(s)",
                        weight=score,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.BUILDER_FLUENT_CHAIN,
                        pattern_category=PatternCategory.CREATIONAL,
                        target_name=t.name,
                        target_kind="class",
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class PrototypeDataCopyRule(BaseRule):
    """Detects Prototype pattern via `data class copy()` or `Cloneable`."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            has_cloneable = "Cloneable" in t.inherited_types
            if t.is_data or has_cloneable:
                evidences = [
                    Evidence(
                        rule_code="CREATIONAL_PROTOTYPE_DATA_COPY",
                        description=f"Type '{t.name}' implements Prototype pattern for instance replication and value transformation",
                        weight=0.85,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.PROTOTYPE_DATA_COPY,
                        pattern_category=PatternCategory.CREATIONAL,
                        target_name=t.name,
                        target_kind="data_class" if t.is_data else "class",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections
