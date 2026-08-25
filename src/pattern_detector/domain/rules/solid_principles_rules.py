"""SOLID principles and clean code quality rules for Kotlin."""

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


class MassiveViewModelSrpRule(BaseRule):
    """Detects Massive ViewModels / God Classes violating Single Responsibility Principle."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            if t.line_count >= 250 or len(t.functions) >= 14 or ("ViewModel" in t.name and len(t.functions) >= 10):
                score = 0.90 if t.line_count >= 300 else 0.80
                evidences = [
                    Evidence(
                        rule_code="SRP_MASSIVE_VIEWMODEL",
                        description=f"Type '{t.name}' is a Massive ViewModel / God Class ({t.line_count} lines, {len(t.functions)} methods, {len(t.properties)} properties) violating SRP",
                        weight=score,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.MASSIVE_VIEWMODEL_SRP,
                        pattern_category=PatternCategory.PRINCIPLE,
                        target_name=t.name,
                        target_kind="class",
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class FatInterfaceIspRule(BaseRule):
    """Detects Fat Interfaces declaring too many required methods violating ISP."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for iface in model.interfaces:
            if len(iface.functions) >= 8:
                evidences = [
                    Evidence(
                        rule_code="ISP_FAT_INTERFACE",
                        description=f"Interface '{iface.name}' is a Fat Interface declaring {len(iface.functions)} required methods; consider splitting into smaller role interfaces",
                        weight=0.85,
                        location=iface.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.FAT_INTERFACE_ISP,
                        pattern_category=PatternCategory.PRINCIPLE,
                        target_name=iface.name,
                        target_kind="interface",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=iface.location,
                        evidences=evidences,
                    )
                )
        return detections


class DynamicCastWhenCascadeOcpRule(BaseRule):
    """Detects repeated `when (x is ...)` typecast cascades violating Open-Closed Principle."""

    WHEN_IS_PATTERN = re.compile(r"\bis\s+[A-Z]\w+\s*->")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            matches = len(self.WHEN_IS_PATTERN.findall(fn.body or ""))
            if matches >= 3:
                evidences = [
                    Evidence(
                        rule_code="OCP_WHEN_IS_CASCADE",
                        description=f"Function '{fn.name}' contains {matches} typecheck branches ('is Type ->'); consider polymorphic dispatch to satisfy OCP",
                        weight=0.85,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.DYNAMIC_CAST_WHEN_CASCADE_OCP,
                        pattern_category=PatternCategory.PRINCIPLE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class KissCyclomaticComplexityRule(BaseRule):
    """Detects functions with excessive cyclomatic complexity."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if fn.branch_count >= 9:
                evidences = [
                    Evidence(
                        rule_code="KISS_CYCLOMATIC_COMPLEXITY",
                        description=f"Function '{fn.name}' has high cyclomatic complexity ({fn.branch_count} branch points), violating KISS",
                        weight=0.88,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.KISS_CYCLOMATIC_COMPLEXITY,
                        pattern_category=PatternCategory.PRINCIPLE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.88, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class KissLongParameterListRule(BaseRule):
    """Detects functions/constructors with excessive parameters."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if len(fn.parameters) >= 5:
                evidences = [
                    Evidence(
                        rule_code="KISS_LONG_PARAMETER_LIST",
                        description=f"Function '{fn.name}' accepts {len(fn.parameters)} parameters; consider using a Data Class or Parameter Object",
                        weight=0.85,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.KISS_LONG_PARAMETER_LIST,
                        pattern_category=PatternCategory.PRINCIPLE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class DryDuplicateLogicRule(BaseRule):
    """Detects duplicated identical algorithmic blocks across functions."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        body_map: dict[str, list[tuple[str, str]]] = {}
        for f in model.files:
            for t in f.types:
                for fn in t.functions:
                    cleaned = re.sub(r"\s+", " ", fn.body).strip()
                    if len(cleaned) >= 50:
                        body_map.setdefault(cleaned, []).append((t.name, fn.name))

        for body, occurrences in body_map.items():
            if len(occurrences) >= 2:
                names = [f"{cls}.{fn}" for cls, fn in occurrences]
                evidences = [
                    Evidence(
                        rule_code="DRY_DUPLICATE_CODE",
                        description=f"Identical logic duplicated across {len(occurrences)} function(s): {', '.join(names[:3])}",
                        weight=0.80,
                        location=None,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.DRY_DUPLICATE_LOGIC,
                        pattern_category=PatternCategory.PRINCIPLE,
                        target_name=names[0],
                        target_kind="function",
                        confidence=Confidence(score=0.80, evidences=evidences),
                        primary_location=None,
                        evidences=evidences,
                    )
                )
        return detections


class DemeterLawTrainWreckRule(BaseRule):
    """Detects Law of Demeter violations (deep object navigation dot chains `a.b.c.d.e`)."""

    DOT_CHAIN_PATTERN = re.compile(r"\b[a-zA-Z_]\w*\.[a-zA-Z_]\w*\.[a-zA-Z_]\w*\.[a-zA-Z_]\w*\.[a-zA-Z_]\w*\b")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            matches = self.DOT_CHAIN_PATTERN.findall(fn.body or "")
            if matches:
                evidences = [
                    Evidence(
                        rule_code="DEMETER_LAW_TRAIN_WRECK",
                        description=f"Function '{fn.name}' violates Law of Demeter with deep navigation chain: '{matches[0]}'",
                        weight=0.80,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.DEMETER_LAW_TRAIN_WRECK,
                        pattern_category=PatternCategory.PRINCIPLE,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.80, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections
