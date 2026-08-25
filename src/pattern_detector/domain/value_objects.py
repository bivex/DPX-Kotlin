"""Value objects and domain enumerations for Kotlin Pattern Detector."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class PatternCategory(str, Enum):
    """Categorization of Kotlin architectural patterns and quality rules."""

    KOTLIN_IDIOMATIC = "kotlin_idiomatic"
    COROUTINES_CONCURRENCY = "coroutines_concurrency"
    COMPOSE_DSL = "compose_dsl"
    CREATIONAL = "creational"
    STRUCTURAL = "structural"
    BEHAVIORAL = "behavioral"
    RESILIENCE = "resilience"
    PRINCIPLE = "principle"


class PatternType(str, Enum):
    """Specific pattern types, idioms, and hazards in Kotlin codebases."""

    # 1. Kotlin Idiomatic & Multiplatform Patterns
    EXTENSION_FUNCTION_ADAPTER = "extension_function_adapter"
    DELEGATED_PROPERTY_LAZY = "delegated_property_lazy"
    SEALED_HIERARCHY_ADT = "sealed_hierarchy_adt"
    INLINE_VALUE_CLASS = "inline_value_class"
    COMPANION_STATIC_FACTORY = "companion_static_factory"
    OPERATOR_OVERLOADING_DSL = "operator_overloading_dsl"
    SCOPE_FUNCTION_CHAIN = "scope_function_chain"

    # 2. Coroutines & Reactive Streams (Structured Concurrency)
    STRUCTURED_CONCURRENCY_SCOPE = "structured_concurrency_scope"
    STATEFLOW_REACTIVE_STREAM = "stateflow_reactive_stream"
    CHANNEL_ACTOR_CONCURRENCY = "channel_actor_concurrency"
    SUSPENDING_FUNCTION_ASYNC = "suspending_function_async"
    DISPATCHER_IO_OFFLOAD = "dispatcher_io_offload"

    # 3. Jetpack Compose & Type-Safe DSL
    TYPE_SAFE_BUILDER_DSL = "type_safe_builder_dsl"
    COMPOSE_DECLARATIVE_VIEW = "compose_declarative_view"
    REMEMBER_MUTABLE_STATE = "remember_mutable_state"
    VIEW_MODEL_STATE_HOLDER = "view_model_state_holder"

    # 4. GoF Creational Patterns (5/5)
    SINGLETON_OBJECT_DECLARATION = "singleton_object_declaration"
    FACTORY_METHOD = "factory_method"
    ABSTRACT_FACTORY = "abstract_factory"
    BUILDER_FLUENT_CHAIN = "builder_fluent_chain"
    PROTOTYPE_DATA_COPY = "prototype_data_copy"

    # 5. GoF Structural Patterns (7/7)
    ADAPTER_INTERFACE_DELEGATION = "adapter_interface_delegation"
    BRIDGE_IMPLEMENTOR = "bridge_implementor"
    COMPOSITE_VIEW_TREE = "composite_view_tree"
    DECORATOR_BY_DELEGATION = "decorator_by_delegation"
    FACADE_COORDINATOR = "facade_coordinator"
    FLYWEIGHT_POOL_CACHE = "flyweight_pool_cache"
    PROXY_VIRTUAL_OR_REMOTE = "proxy_virtual_or_remote"

    # 6. GoF Behavioral Patterns (11/11)
    CHAIN_OF_RESPONSIBILITY = "chain_of_responsibility"
    COMMAND_ACTION_OBJECT = "command_action_object"
    INTERPRETER_EXPRESSION_AST = "interpreter_expression_ast"
    ITERATOR_SEQUENCE_FLOW = "iterator_sequence_flow"
    MEDIATOR_COORDINATOR = "mediator_coordinator"
    MEMENTO_SERIALIZABLE_STATE = "memento_serializable_state"
    OBSERVER_FLOW_PUBLISHED = "observer_flow_published"
    STATE_SEALED_CLASS_FSM = "state_sealed_class_fsm"
    STRATEGY_LAMBDA_INJECTION = "strategy_lambda_injection"
    TEMPLATE_METHOD_ALGORITHM = "template_method_algorithm"
    VISITOR_SEALED_WHEN = "visitor_sealed_when"

    # 7. Resilience, Safety & Hazards
    GLOBALSCOPE_COROUTINE_LEAK = "globalscope_coroutine_leak"
    NON_CANCELLATION_EXCEPTION_SWALLOW = "non_cancellation_exception_swallow"
    FORCE_NULL_ASSERTION_HAZARD = "force_null_assertion_hazard"
    FORCE_CAST_HAZARD = "force_cast_hazard"
    MAIN_THREAD_BLOCKING_CALL = "main_thread_blocking_call"
    STRONG_CONTEXT_LEAK = "strong_context_leak"

    # 8. SOLID & Clean Architecture Principles
    MASSIVE_VIEWMODEL_SRP = "massive_viewmodel_srp"
    FAT_INTERFACE_ISP = "fat_interface_isp"
    DYNAMIC_CAST_WHEN_CASCADE_OCP = "dynamic_cast_when_cascade_ocp"
    KISS_CYCLOMATIC_COMPLEXITY = "kiss_cyclomatic_complexity"
    KISS_LONG_PARAMETER_LIST = "kiss_long_parameter_list"
    DRY_DUPLICATE_LOGIC = "dry_duplicate_logic"
    DEMETER_LAW_TRAIN_WRECK = "demeter_law_train_wreck"


class ConfidenceLevel(str, Enum):
    """Normalized confidence tiers for detection ranking."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    VERY_HIGH = "VERY_HIGH"


@dataclass(frozen=True)
class SourceLocation:
    """Precise source code location in a Kotlin file."""

    file_path: str
    line: int
    column: int = 1

    def __str__(self) -> str:
        return f"{self.file_path}:{self.line}:{self.column}"


@dataclass(frozen=True)
class Evidence:
    """Individual heuristic signal contributing to pattern confidence."""

    rule_code: str
    description: str
    weight: float
    location: SourceLocation | None = None


@dataclass
class Confidence:
    """Calculated confidence rating aggregating evidence items."""

    score: float
    evidences: list[Evidence] = field(default_factory=list)

    @property
    def level(self) -> ConfidenceLevel:
        if self.score >= 0.85:
            return ConfidenceLevel.VERY_HIGH
        if self.score >= 0.70:
            return ConfidenceLevel.HIGH
        if self.score >= 0.50:
            return ConfidenceLevel.MEDIUM
        return ConfidenceLevel.LOW

    @property
    def percentage(self) -> int:
        return int(round(self.score * 100))

    @property
    def percentage_str(self) -> str:
        return f"{self.percentage}%"
