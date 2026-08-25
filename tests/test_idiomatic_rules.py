"""Unit tests for Kotlin Idiomatic pattern detection rules."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_kotlin_parser import NativeKotlinParserAdapter
from pattern_detector.domain.rules.idiomatic_rules import (
    CompanionStaticFactoryRule,
    DelegatedPropertyLazyRule,
    ExtensionFunctionAdapterRule,
    InlineValueClassRule,
    OperatorOverloadingDslRule,
    ScopeFunctionChainRule,
    SealedHierarchyAdtRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_extension_function_adapter() -> None:
    code = """
    package com.example.util

    fun String.toSlug(): String {
        return this.lowercase().replace(" ", "-")
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("StringUtils.kt", code)])

    rule = ExtensionFunctionAdapterRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.EXTENSION_FUNCTION_ADAPTER
    assert detections[0].target_name == "String.toSlug"


def test_delegated_property_lazy() -> None:
    code = """
    package com.example.app

    class ServiceClient {
        val httpClient: HttpClient by lazy {
            HttpClient()
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("ServiceClient.kt", code)])

    rule = DelegatedPropertyLazyRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.DELEGATED_PROPERTY_LAZY
    assert detections[0].target_name == "httpClient"


def test_sealed_hierarchy_adt() -> None:
    code = """
    package com.example.domain

    sealed class NetworkResult<out T> {
        data class Success<out T>(val data: T) : NetworkResult<T>()
        data class Error(val exception: Throwable) : NetworkResult<Nothing>()
        object Loading : NetworkResult<Nothing>()
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("NetworkResult.kt", code)])

    rule = SealedHierarchyAdtRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.SEALED_HIERARCHY_ADT
    assert detections[0].target_name == "NetworkResult"


def test_inline_value_class() -> None:
    code = """
    package com.example.domain

    @JvmInline
    value class AccountId(val rawValue: String)
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("AccountId.kt", code)])

    rule = InlineValueClassRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.INLINE_VALUE_CLASS
    assert detections[0].target_name == "AccountId"


def test_companion_static_factory() -> None:
    code = """
    package com.example.domain

    class User private constructor(val id: String, val email: String) {
        companion object {
            fun create(email: String): User {
                return User(UUID.randomUUID().toString(), email)
            }
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("User.kt", code)])

    rule = CompanionStaticFactoryRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.COMPANION_STATIC_FACTORY


def test_operator_overloading_dsl() -> None:
    code = """
    package com.example.math

    data class Money(val amount: Double) {
        operator fun plus(other: Money): Money {
            return Money(this.amount + other.amount)
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("Money.kt", code)])

    rule = OperatorOverloadingDslRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.OPERATOR_OVERLOADING_DSL


def test_scope_function_chain() -> None:
    code = """
    package com.example.service

    fun configureClient(): Client {
        return Client().apply {
            timeout = 30
        }.also {
            logger.info("Configured")
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("Config.kt", code)])

    rule = ScopeFunctionChainRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.SCOPE_FUNCTION_CHAIN
