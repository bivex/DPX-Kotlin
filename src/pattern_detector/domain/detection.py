"""Detection result and summary aggregates for Kotlin Pattern Detector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from pattern_detector.domain.pattern import PATTERN_CATALOG
from pattern_detector.domain.value_objects import (
    Confidence,
    ConfidenceLevel,
    Evidence,
    PatternCategory,
    PatternType,
    SourceLocation,
)


@dataclass
class Detection:
    """Individual pattern instance or architectural signal identified in Kotlin source."""

    pattern_type: PatternType
    pattern_category: PatternCategory
    target_name: str
    target_kind: str  # class, interface, object, function, property, file
    confidence: Confidence
    primary_location: SourceLocation | None = None
    related_locations: list[SourceLocation] = field(default_factory=list)
    evidences: list[Evidence] = field(default_factory=list)

    @property
    def level(self) -> ConfidenceLevel:
        return self.confidence.level

    @property
    def summary(self) -> str:
        pdef = PATTERN_CATALOG.get(self.pattern_type)
        if pdef:
            return pdef.description
        return f"Pattern {self.pattern_type.value} detected on {self.target_kind} '{self.target_name}'"

    def to_dict(self) -> dict[str, Any]:
        return {
            "pattern_type": self.pattern_type.value,
            "pattern_category": self.pattern_category.value,
            "target_name": self.target_name,
            "target_kind": self.target_kind,
            "confidence": {
                "score": self.confidence.score,
                "percentage": self.confidence.percentage_str,
                "level": self.level.value,
            },
            "primary_location": {
                "file_path": self.primary_location.file_path,
                "line": self.primary_location.line,
                "column": self.primary_location.column,
            } if self.primary_location else None,
            "related_locations": [
                {
                    "file_path": loc.file_path,
                    "line": loc.line,
                    "column": loc.column,
                }
                for loc in self.related_locations
            ],
            "evidences": [
                {
                    "rule_code": ev.rule_code,
                    "description": ev.description,
                    "weight": ev.weight,
                    "location": {
                        "file_path": ev.location.file_path,
                        "line": ev.location.line,
                        "column": ev.location.column,
                    } if ev.location else None,
                }
                for ev in self.evidences
            ],
        }


@dataclass
class DetectionReport:
    """Aggregate scan report for a Kotlin codebase."""

    project_path: str
    scanned_files_count: int
    detections: list[Detection] = field(default_factory=list)
    elapsed_seconds: float = 0.0

    @property
    def total_detections_count(self) -> int:
        return len(self.detections)

    @property
    def summary_by_category(self) -> dict[str, int]:
        summary: dict[str, int] = {cat.value: 0 for cat in PatternCategory}
        for d in self.detections:
            summary[d.pattern_category.value] = summary.get(d.pattern_category.value, 0) + 1
        return summary

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_path": self.project_path,
            "scanned_files_count": self.scanned_files_count,
            "total_detections_count": self.total_detections_count,
            "elapsed_seconds": self.elapsed_seconds,
            "summary_by_category": self.summary_by_category,
            "detections": [d.to_dict() for d in self.detections],
        }
