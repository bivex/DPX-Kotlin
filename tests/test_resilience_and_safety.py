"""Unit tests for Kotlin & Android memory safety, coroutine leaks, and hazard rules."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_kotlin_parser import NativeKotlinParserAdapter
from pattern_detector.domain.rules.resilience_safety_rules import (
    ForceCastHazardRule,
    ForceNullAssertionHazardRule,
    GlobalScopeCoroutineLeakRule,
    MainThreadBlockingCallRule,
    NonCancellationExceptionSwallowRule,
    StrongContextLeakRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_globalscope_coroutine_leak() -> None:
    code = """
    package com.example.leak

    fun fireAndForget() {
        GlobalScope.launch {
            doBackgroundSync()
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("Leak.kt", code)])

    rule = GlobalScopeCoroutineLeakRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.GLOBALSCOPE_COROUTINE_LEAK


def test_non_cancellation_exception_swallow() -> None:
    code = """
    package com.example.coroutine

    suspend fun fetchData() {
        try {
            api.call()
        } catch (e: Exception) {
            println("error")
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("Fetch.kt", code)])

    rule = NonCancellationExceptionSwallowRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.NON_CANCELLATION_EXCEPTION_SWALLOW


def test_force_null_assertion_hazard() -> None:
    code = """
    package com.example.nulls

    fun printName(user: User?) {
        val name = user!!.name
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("Nulls.kt", code)])

    rule = ForceNullAssertionHazardRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.FORCE_NULL_ASSERTION_HAZARD


def test_force_cast_hazard() -> None:
    code = """
    package com.example.cast

    fun processEvent(e: Any) {
        val click = e as ClickEvent
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("Cast.kt", code)])

    rule = ForceCastHazardRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.FORCE_CAST_HAZARD


def test_main_thread_blocking_call() -> None:
    code = """
    package com.example.ui

    class HomeViewModel : ViewModel() {
        fun loadSync() {
            Thread.sleep(1000)
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("HomeViewModel.kt", code)])

    rule = MainThreadBlockingCallRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.MAIN_THREAD_BLOCKING_CALL


def test_strong_context_leak() -> None:
    code = """
    package com.example.leak

    object AppManager {
        var context: Context? = null
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("AppManager.kt", code)])

    rule = StrongContextLeakRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.STRONG_CONTEXT_LEAK
