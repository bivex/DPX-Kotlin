"""Outbound driven ports for DPX-Kotlin."""

from __future__ import annotations

from typing import Protocol
from pattern_detector.domain.code_model import CodeModel, KotlinFile
from pattern_detector.domain.detection import DetectionReport


class SourceProviderPort(Protocol):
    """Port for discovering and loading Kotlin source files."""

    def load_files(self, target_path: str, extensions: list[str], exclude_dirs: list[str] | None = None) -> list[tuple[str, str]]:
        """Return list of (file_path, file_content)."""
        ...


class ParserPort(Protocol):
    """Port for parsing Kotlin source text into CodeModel."""

    def parse_file(self, file_path: str, content: str) -> KotlinFile:
        """Parse a single Kotlin file into KotlinFile model."""
        ...

    def parse_codebase(self, files: list[tuple[str, str]], target_path: str = "") -> CodeModel:
        """Parse multiple Kotlin files into an aggregated CodeModel."""
        ...


class ReportFormatterPort(Protocol):
    """Port for formatting DetectionReport into text, HTML, Markdown, etc."""

    def format(self, report: DetectionReport, verbose: bool = False) -> str:
        """Format report into string representation."""
        ...


class ResultRepositoryPort(Protocol):
    """Port for persisting formatted detection reports to disk."""

    def save(self, report: DetectionReport, destination_path: str, verbose: bool = False) -> None:
        """Save report to destination path."""
        ...
