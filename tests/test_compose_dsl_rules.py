"""Unit tests for Jetpack Compose & Type-Safe DSL rules in Kotlin."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_kotlin_parser import NativeKotlinParserAdapter
from pattern_detector.domain.rules.compose_dsl_rules import (
    ComposeDeclarativeViewRule,
    RememberMutableStateRule,
    TypeSafeBuilderDslRule,
    ViewModelStateHolderRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_type_safe_builder_dsl() -> None:
    code = """
    package com.example.dsl

    fun html(init: HTML.() -> Unit): HTML {
        val html = HTML()
        html.init()
        return html
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("HtmlDsl.kt", code)])

    rule = TypeSafeBuilderDslRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.TYPE_SAFE_BUILDER_DSL
    assert detections[0].target_name == "html"


def test_compose_declarative_view() -> None:
    code = """
    package com.example.ui

    @Composable
    fun UserCard(user: User) {
        Column {
            Text(user.name)
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("UserCard.kt", code)])

    rule = ComposeDeclarativeViewRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.COMPOSE_DECLARATIVE_VIEW
    assert detections[0].target_name == "UserCard"


def test_remember_mutable_state() -> None:
    code = """
    package com.example.ui

    @Composable
    fun CounterScreen() {
        var count by remember { mutableStateOf(0) }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("CounterScreen.kt", code)])

    rule = RememberMutableStateRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.REMEMBER_MUTABLE_STATE


def test_view_model_state_holder() -> None:
    code = """
    package com.example.ui

    class ProfileViewModel : ViewModel() {
        fun loadProfile() {}
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("ProfileViewModel.kt", code)])

    rule = ViewModelStateHolderRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.VIEW_MODEL_STATE_HOLDER
    assert detections[0].target_name == "ProfileViewModel"
