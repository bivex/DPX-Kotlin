"""GoF Structural design pattern detection rules for Kotlin (7/7)."""

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


class AdapterInterfaceDelegationRule(BaseRule):
    """Detects Adapter pattern adapting third-party/legacy types to domain interfaces."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            if "Adapter" in t.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_ADAPTER_PATTERN",
                        description=f"Class '{t.name}' adapts target interface to domain contracts",
                        weight=0.85,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.ADAPTER_INTERFACE_DELEGATION,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=t.name,
                        target_kind="class",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class BridgeImplementorRule(BaseRule):
    """Detects Bridge pattern decoupling abstraction from implementor."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            impl_props = [
                p for p in t.properties
                if any(suffix in p.type_name for suffix in ("Implementor", "Renderer", "Driver", "Engine"))
            ]
            if impl_props or "Bridge" in t.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_BRIDGE_PATTERN",
                        description=f"Class '{t.name}' decouples abstraction from implementor via '{impl_props[0].name if impl_props else 'implementor'}'",
                        weight=0.85,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.BRIDGE_IMPLEMENTOR,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=t.name,
                        target_kind="class",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class CompositeViewTreeRule(BaseRule):
    """Detects Composite pattern in tree structures and UI components."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            has_children = any(
                p.type_name in (f"List<{t.name}>", f"Set<{t.name}>", f"Collection<{t.name}>")
                or "children" in p.name.lower() or "components" in p.name.lower()
                for p in t.properties
            )
            if has_children or "Composite" in t.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_COMPOSITE_TREE",
                        description=f"Class '{t.name}' implements Composite pattern hosting recursive child component hierarchy",
                        weight=0.85,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.COMPOSITE_VIEW_TREE,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=t.name,
                        target_kind="class",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class DecoratorByDelegationRule(BaseRule):
    """Detects Decorator pattern via Kotlin interface delegation (`class Foo(...) : Bar by underlying`)."""

    DECORATOR_DELEGATION_PATTERN = re.compile(r":\s*[A-Za-z0-9_]+\s+by\s+[A-Za-z0-9_]+")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            if self.DECORATOR_DELEGATION_PATTERN.search(t.raw_text or "") or "Decorator" in t.name:
                score = 0.95 if self.DECORATOR_DELEGATION_PATTERN.search(t.raw_text or "") else 0.80
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_DECORATOR_BY_DELEGATION",
                        description=f"Class '{t.name}' decorates underlying instance using first-class Kotlin interface delegation ('by')",
                        weight=score,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.DECORATOR_BY_DELEGATION,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=t.name,
                        target_kind="class",
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class FacadeCoordinatorRule(BaseRule):
    """Detects Facade Coordinator orchestrating multiple repositories, services, or use cases."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            subsystem_deps = [
                p for p in t.properties
                if any(suffix in p.type_name for suffix in ("Repository", "Service", "Client", "Store", "UseCase", "Provider"))
            ]
            if len(subsystem_deps) >= 2 or "Facade" in t.name:
                score = 0.90 if "Facade" in t.name else 0.80
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_FACADE_COORDINATOR",
                        description=f"Class '{t.name}' coordinates {len(subsystem_deps)} subsystem dependencies as a unified Facade",
                        weight=score,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.FACADE_COORDINATOR,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=t.name,
                        target_kind="class",
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class FlyweightPoolCacheRule(BaseRule):
    """Detects Flyweight pattern sharing instances via dictionary pool or factory caching."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_types:
            has_cache_prop = any("cache" in p.name.lower() or "pool" in p.name.lower() for p in t.properties)
            if "Flyweight" in t.name or (has_cache_prop and any(fn.name.startswith("get") or fn.name.startswith("make") for fn in t.functions)):
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_FLYWEIGHT_CACHE",
                        description=f"Type '{t.name}' shares fine-grained instances via Flyweight pooling cache",
                        weight=0.85,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.FLYWEIGHT_POOL_CACHE,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=t.name,
                        target_kind=t.kind,
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class ProxyVirtualOrRemoteRule(BaseRule):
    """Detects Proxy pattern controlling access to an underlying target."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            if "Proxy" in t.name:
                evidences = [
                    Evidence(
                        rule_code="STRUCTURAL_PROXY_PATTERN",
                        description=f"Class '{t.name}' acts as surrogate Proxy controlling access to target service",
                        weight=0.85,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.PROXY_VIRTUAL_OR_REMOTE,
                        pattern_category=PatternCategory.STRUCTURAL,
                        target_name=t.name,
                        target_kind="class",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections
