"""Unit tests verifying zero false positives on clean, idiomatic Kotlin code."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_kotlin_parser import NativeKotlinParserAdapter
from pattern_detector.domain.rules import get_default_rules
from pattern_detector.domain.rules.creational_rules import (
    FactoryMethodRule,
    SingletonObjectDeclarationRule,
)
from pattern_detector.domain.rules.resilience_safety_rules import (
    ForceCastHazardRule,
    ForceNullAssertionHazardRule,
    GlobalScopeCoroutineLeakRule,
    MainThreadBlockingCallRule,
    NonCancellationExceptionSwallowRule,
    StrongContextLeakRule,
)
from pattern_detector.domain.rules.solid_principles_rules import (
    FatInterfaceIspRule,
    KissCyclomaticComplexityRule,
    KissLongParameterListRule,
    MassiveViewModelSrpRule,
)
from pattern_detector.domain.services.rule_engine import RuleEngineService
from pattern_detector.domain.value_objects import PatternCategory


def test_plain_data_class_no_srp_violations() -> None:
    code = """
    package com.example.model

    data class Customer(
        val id: String,
        val firstName: String,
        val lastName: String,
        val email: String,
        val isVerified: Boolean
    )
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("Customer.kt", code)])

    rule = MassiveViewModelSrpRule()
    detections = rule.evaluate(model)

    assert len(detections) == 0


def test_safe_null_handling_no_force_null_hazard() -> None:
    code = """
    package com.example.util

    fun processUser(user: User?) {
        val name = user?.name ?: "Unknown"
        user?.let {
            println(it.email)
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("Process.kt", code)])

    rule = ForceNullAssertionHazardRule()
    detections = rule.evaluate(model)

    assert len(detections) == 0


def test_safe_cast_no_force_cast_hazard() -> None:
    code = """
    package com.example.util

    fun parseItem(item: Any?): String? {
        val text = item as? String
        return text?.trim()
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("SafeCast.kt", code)])

    rule = ForceCastHazardRule()
    detections = rule.evaluate(model)

    assert len(detections) == 0


def test_structured_coroutine_scope_no_globalscope_hazard() -> None:
    code = """
    package com.example.vm

    class TaskViewModel(private val scope: CoroutineScope) : ViewModel() {
        fun runTask() {
            scope.launch {
                execute()
            }
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("TaskViewModel.kt", code)])

    rule = GlobalScopeCoroutineLeakRule()
    detections = rule.evaluate(model)

    assert len(detections) == 0


def test_rethrowing_cancellation_exception_no_swallow_hazard() -> None:
    code = """
    package com.example.service

    suspend fun safeApiCall() {
        try {
            api.fetch()
        } catch (e: Exception) {
            if (e is CancellationException) throw e
            logger.error("Error: $e")
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("SafeApi.kt", code)])

    rule = NonCancellationExceptionSwallowRule()
    detections = rule.evaluate(model)

    assert len(detections) == 0


def test_pure_domain_validator_no_hazards() -> None:
    code = """
    package com.example.validator

    class OrderValidator {
        fun validate(amount: Double): Boolean {
            return amount > 0.0
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("OrderValidator.kt", code)])

    engine = RuleEngineService(rules=get_default_rules())
    detections = engine.evaluate(model)

    hazards = [d for d in detections if d.pattern_category in (PatternCategory.RESILIENCE, PatternCategory.PRINCIPLE)]
    assert len(hazards) == 0
