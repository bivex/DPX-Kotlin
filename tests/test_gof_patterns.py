"""Unit tests for all 23 GoF Creational, Structural, and Behavioral patterns in Kotlin."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_kotlin_parser import NativeKotlinParserAdapter
from pattern_detector.domain.rules.behavioral_rules import (
    ChainOfResponsibilityRule,
    CommandActionObjectRule,
    InterpreterExpressionAstRule,
    IteratorSequenceFlowRule,
    MediatorCoordinatorRule,
    MementoSerializableStateRule,
    ObserverFlowPublishedRule,
    StateSealedClassFsmRule,
    StrategyLambdaInjectionRule,
    TemplateMethodAlgorithmRule,
    VisitorSealedWhenRule,
)
from pattern_detector.domain.rules.creational_rules import (
    AbstractFactoryRule,
    BuilderFluentChainRule,
    FactoryMethodRule,
    PrototypeDataCopyRule,
    SingletonObjectDeclarationRule,
)
from pattern_detector.domain.rules.structural_rules import (
    AdapterInterfaceDelegationRule,
    BridgeImplementorRule,
    CompositeViewTreeRule,
    DecoratorByDelegationRule,
    FacadeCoordinatorRule,
    FlyweightPoolCacheRule,
    ProxyVirtualOrRemoteRule,
)
from pattern_detector.domain.value_objects import PatternType


# --- Creational (5/5) ---

def test_singleton_object_declaration() -> None:
    code = """
    package com.example.config

    object DatabaseConfig {
        val jdbcUrl = "jdbc:sqlite:app.db"
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("DatabaseConfig.kt", code)])

    rule = SingletonObjectDeclarationRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.SINGLETON_OBJECT_DECLARATION
    assert detections[0].target_name == "DatabaseConfig"


def test_factory_method() -> None:
    code = """
    package com.example.factory

    class DialogFactory {
        fun createDialog(): Dialog {
            return CustomDialog()
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("DialogFactory.kt", code)])

    rule = FactoryMethodRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.FACTORY_METHOD


def test_abstract_factory() -> None:
    code = """
    package com.example.factory

    interface GUIFactory {
        fun createButton(): Button
        fun createCheckbox(): Checkbox
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("GUIFactory.kt", code)])

    rule = AbstractFactoryRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.ABSTRACT_FACTORY


def test_builder_fluent_chain() -> None:
    code = """
    package com.example.builder

    class HttpRequestBuilder {
        fun withHeader(k: String, v: String): HttpRequestBuilder = this
        fun setTimeout(ms: Long): HttpRequestBuilder = this
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("RequestBuilder.kt", code)])

    rule = BuilderFluentChainRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.BUILDER_FLUENT_CHAIN


def test_prototype_data_copy() -> None:
    code = """
    package com.example.model

    data class UserProfile(val id: String, val name: String)
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("UserProfile.kt", code)])

    rule = PrototypeDataCopyRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.PROTOTYPE_DATA_COPY


# --- Structural (7/7) ---

def test_adapter_pattern() -> None:
    code = """
    package com.example.adapter

    class LegacyLoggerAdapter : AppLogger
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("LoggerAdapter.kt", code)])

    rule = AdapterInterfaceDelegationRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.ADAPTER_INTERFACE_DELEGATION


def test_bridge_pattern() -> None:
    code = """
    package com.example.bridge

    class WindowRenderer(private val graphicsEngine: GraphicsEngine)
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("WindowRenderer.kt", code)])

    rule = BridgeImplementorRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.BRIDGE_IMPLEMENTOR


def test_composite_pattern() -> None:
    code = """
    package com.example.tree

    class ViewGroup : UIElement {
        val children: List<UIElement> = listOf()
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("ViewGroup.kt", code)])

    rule = CompositeViewTreeRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.COMPOSITE_VIEW_TREE


def test_decorator_by_delegation() -> None:
    code = """
    package com.example.decorator

    class LoggingService(private val target: Service) : Service by target
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("LoggingService.kt", code)])

    rule = DecoratorByDelegationRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.DECORATOR_BY_DELEGATION


def test_facade_coordinator() -> None:
    code = """
    package com.example.facade

    class OrderFacade(
        private val paymentService: PaymentService,
        private val inventoryRepository: InventoryRepository
    )
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("OrderFacade.kt", code)])

    rule = FacadeCoordinatorRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.FACADE_COORDINATOR


def test_flyweight_cache() -> None:
    code = """
    package com.example.cache

    class FontFlyweightFactory {
        private val cache = mutableMapOf<String, Font>()
        fun getFont(name: String): Font = cache[name]!!
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("FontFactory.kt", code)])

    rule = FlyweightPoolCacheRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.FLYWEIGHT_POOL_CACHE


def test_proxy_pattern() -> None:
    code = """
    package com.example.proxy

    class RemoteImageProxy : Image
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("ImageProxy.kt", code)])

    rule = ProxyVirtualOrRemoteRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.PROXY_VIRTUAL_OR_REMOTE


# --- Behavioral (11/11) ---

def test_chain_of_responsibility() -> None:
    code = """
    package com.example.chain

    class AuthInterceptor {
        var nextHandler: AuthInterceptor? = null
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("AuthInterceptor.kt", code)])

    rule = ChainOfResponsibilityRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.CHAIN_OF_RESPONSIBILITY


def test_command_action() -> None:
    code = """
    package com.example.command

    class SaveDocumentCommand {
        fun execute() {}
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("SaveCommand.kt", code)])

    rule = CommandActionObjectRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.COMMAND_ACTION_OBJECT


def test_interpreter_expression_ast() -> None:
    code = """
    package com.example.ast

    class AddExpression {
        fun interpret(context: EvalContext): Int = 42
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("AddExpression.kt", code)])

    rule = InterpreterExpressionAstRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.INTERPRETER_EXPRESSION_AST


def test_iterator_sequence() -> None:
    code = """
    package com.example.seq

    class CustomRangeSequence : Sequence<Int> {
        override fun iterator(): Iterator<Int> = TODO()
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("RangeSeq.kt", code)])

    rule = IteratorSequenceFlowRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.ITERATOR_SEQUENCE_FLOW


def test_mediator_coordinator() -> None:
    code = """
    package com.example.nav

    class MainAppCoordinator {
        fun startFlow() {}
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("Coordinator.kt", code)])

    rule = MediatorCoordinatorRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.MEDIATOR_COORDINATOR


def test_memento_serializable() -> None:
    code = """
    package com.example.state

    @Serializable
    data class EditorSnapshot(val text: String, val cursor: Int)
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("Snapshot.kt", code)])

    rule = MementoSerializableStateRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.MEMENTO_SERIALIZABLE_STATE


def test_observer_flow_published() -> None:
    code = """
    package com.example.feed

    class NewsFeedService {
        val updatesFlow: Flow<NewsItem> = emptyFlow()
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("NewsFeed.kt", code)])

    rule = ObserverFlowPublishedRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.OBSERVER_FLOW_PUBLISHED


def test_state_sealed_class_fsm() -> None:
    code = """
    package com.example.state

    sealed class AuthState {
        object Idle : AuthState()
        data class Authenticated(val token: String) : AuthState()
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("AuthState.kt", code)])

    rule = StateSealedClassFsmRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.STATE_SEALED_CLASS_FSM


def test_strategy_lambda_injection() -> None:
    code = """
    package com.example.strategy

    class PaymentProcessor(private val strategy: PaymentStrategy)
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("PaymentProcessor.kt", code)])

    rule = StrategyLambdaInjectionRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.STRATEGY_LAMBDA_INJECTION


def test_template_method_algorithm() -> None:
    code = """
    package com.example.template

    abstract class DataPipelineTemplate {
        fun processPipeline() {
            stepRead()
            stepTransform()
            stepWrite()
        }
        abstract fun stepRead()
        abstract fun stepTransform()
        abstract fun stepWrite()
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("DataPipeline.kt", code)])

    rule = TemplateMethodAlgorithmRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.TEMPLATE_METHOD_ALGORITHM


def test_visitor_sealed_when() -> None:
    code = """
    package com.example.visitor

    class SyntaxNode {
        fun accept(visitor: ASTVisitor) {}
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("SyntaxNode.kt", code)])

    rule = VisitorSealedWhenRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.VISITOR_SEALED_WHEN
