"""Unit tests for SOLID principles and code quality rules in Kotlin."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_kotlin_parser import NativeKotlinParserAdapter
from pattern_detector.domain.rules.solid_principles_rules import (
    DynamicCastWhenCascadeOcpRule,
    FatInterfaceIspRule,
    KissCyclomaticComplexityRule,
    KissLongParameterListRule,
    MassiveViewModelSrpRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_massive_viewmodel_srp() -> None:
    methods_code = "\n".join(f"fun method{i}() {{}}" for i in range(16))
    code = f"""
    package com.example.ui

    class OrderViewModel : ViewModel() {{
        {methods_code}
    }}
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("OrderViewModel.kt", code)])

    rule = MassiveViewModelSrpRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.MASSIVE_VIEWMODEL_SRP
    assert detections[0].target_name == "OrderViewModel"


def test_fat_interface_isp() -> None:
    methods_code = "\n".join(f"fun req{i}()" for i in range(10))
    code = f"""
    package com.example.service

    interface MegaService {{
        {methods_code}
    }}
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("MegaService.kt", code)])

    rule = FatInterfaceIspRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.FAT_INTERFACE_ISP


def test_dynamic_cast_when_cascade_ocp() -> None:
    code = """
    package com.example.handler

    fun handleEvent(e: Event) {
        when (e) {
            is ClickEvent -> handleClick()
            is HoverEvent -> handleHover()
            is ScrollEvent -> handleScroll()
            is DragEvent -> handleDrag()
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("EventHandler.kt", code)])

    rule = DynamicCastWhenCascadeOcpRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.DYNAMIC_CAST_WHEN_CASCADE_OCP


def test_kiss_long_parameter_list() -> None:
    code = """
    package com.example.config

    fun configureServer(host: String, port: Int, timeout: Long, maxConnections: Int, sslEnabled: Boolean) {
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("ServerConfig.kt", code)])

    rule = KissLongParameterListRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.KISS_LONG_PARAMETER_LIST


def test_kiss_cyclomatic_complexity() -> None:
    branches = "\n".join(f"if (x == {i}) {{ println({i}) }}" for i in range(11))
    code = f"""
    package com.example.math

    fun complexBranching(x: Int) {{
        {branches}
    }}
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("Complex.kt", code)])

    rule = KissCyclomaticComplexityRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.KISS_CYCLOMATIC_COMPLEXITY
