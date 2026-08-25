"""Console Rich Formatter for Kotlin pattern detection findings."""

from __future__ import annotations

import io
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree

from pattern_detector.domain.detection import DetectionReport
from pattern_detector.domain.pattern import PATTERN_CATALOG
from pattern_detector.domain.value_objects import ConfidenceLevel
from pattern_detector.ports.outbound import ReportFormatterPort


class ConsoleReportFormatter(ReportFormatterPort):
    """Renders findings to interactive terminal using Rich."""

    def format(self, report: DetectionReport, verbose: bool = False) -> str:
        string_io = io.StringIO()
        console = Console(file=string_io, force_terminal=True, color_system="truecolor", width=120)

        # Header Banner
        header = Panel.fit(
            f"[bold white]🎯 DPX-Kotlin: Coroutines, Flow, Compose & Multiplatform Architectural Detector (Kotlin 1.8 - 2.0+)[/bold white]\n"
            f"[dim]Target: {report.project_path} | Scanned: {report.scanned_files_count} file(s) in {report.elapsed_seconds:.3f}s | Findings: {report.total_detections_count}[/dim]",
            border_style="magenta",
        )
        console.print(header)

        # Summary Table
        table = Table(title="📊 Detection Summary by Category", title_style="bold magenta", border_style="dim")
        table.add_column("Pattern Category", style="bold white")
        table.add_column("Detections", justify="right", style="bold yellow")
        table.add_column("Confidence Breakdown", style="dim")

        for cat, count in sorted(report.summary_by_category.items(), key=lambda x: -x[1]):
            if count == 0:
                continue
            cat_dets = [d for d in report.detections if d.pattern_category.value == cat]
            vh = sum(1 for d in cat_dets if d.level == ConfidenceLevel.VERY_HIGH)
            h = sum(1 for d in cat_dets if d.level == ConfidenceLevel.HIGH)
            m = sum(1 for d in cat_dets if d.level == ConfidenceLevel.MEDIUM)
            l = sum(1 for d in cat_dets if d.level == ConfidenceLevel.LOW)
            breakdown = f"{vh} VERY HIGH, {h} HIGH, {m} MED, {l} LOW"
            table.add_row(cat.upper(), str(count), breakdown)

        console.print(table)
        console.print("\n[bold]📋 Identified Architectural Patterns & Resilience Signals:[/bold]\n")

        for idx, det in enumerate(report.detections, 1):
            level_color = {
                ConfidenceLevel.VERY_HIGH: "bold green",
                ConfidenceLevel.HIGH: "bold cyan",
                ConfidenceLevel.MEDIUM: "bold yellow",
                ConfidenceLevel.LOW: "bold red",
            }.get(det.level, "white")

            tree = Tree(f"[bold white]#{idx} {det.pattern_type.value.upper()}[/bold white] on [magenta]{det.target_kind}[/magenta] '[bold white]{det.target_name}[/bold white]'")
            if det.primary_location:
                tree.add(f"📍 [dim]Location:[/dim] [yellow]{det.primary_location}[/yellow]")
            tree.add(f"🎯 [dim]Confidence:[/dim] [{level_color}]{det.confidence.percentage_str} [{det.level.value}][/{level_color}]")
            tree.add(f"📝 [dim]Summary:[/dim] {det.summary}")

            if det.evidences:
                ev_branch = tree.add(f"🔎 [dim]Evidence Trail ({len(det.evidences)} heuristics):[/dim]")
                for ev in det.evidences:
                    pct = int(ev.weight * 100)
                    loc_str = f" → [yellow]{ev.location}[/yellow]" if ev.location else ""
                    ev_branch.add(f"[green]+{pct}%[/green] [dim]({ev.rule_code})[/dim] {ev.description}{loc_str}")

            console.print(tree)
            console.print("")

        return string_io.getvalue()
