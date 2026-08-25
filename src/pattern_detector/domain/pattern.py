"""Kotlin architectural patterns catalog with descriptions and GoF equivalents."""

from __future__ import annotations

from dataclasses import dataclass
from pattern_detector.domain.value_objects import PatternCategory, PatternType


@dataclass(frozen=True)
class PatternDefinition:
    """Catalog entry describing a Kotlin architectural pattern."""

    type: PatternType
    category: PatternCategory
    name: str
    description: str
    gof_equivalent: str | None = None
    kotlin_version: str = "1.8 - 2.0+"
    recommendation: str | None = None


PATTERN_CATALOG: dict[PatternType, PatternDefinition] = {
    # 1. Kotlin Idiomatic Patterns
    PatternType.EXTENSION_FUNCTION_ADAPTER: PatternDefinition(
        type=PatternType.EXTENSION_FUNCTION_ADAPTER,
        category=PatternCategory.KOTLIN_IDIOMATIC,
        name="Extension Function / Property Adapter",
        description="Retroactive extension augmenting types with domain methods without subclassing.",
        gof_equivalent="Adapter / Decorator",
    ),
    PatternType.DELEGATED_PROPERTY_LAZY: PatternDefinition(
        type=PatternType.DELEGATED_PROPERTY_LAZY,
        category=PatternCategory.KOTLIN_IDIOMATIC,
        name="Delegated Property (`by lazy` / Custom Delegate)",
        description="Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.",
        gof_equivalent="Proxy / Lazy Initialization",
    ),
    PatternType.SEALED_HIERARCHY_ADT: PatternDefinition(
        type=PatternType.SEALED_HIERARCHY_ADT,
        category=PatternCategory.KOTLIN_IDIOMATIC,
        name="Sealed Class / Interface ADT Hierarchy",
        description="Exhaustive sum types / Algebraic Data Types representing closed polymorphic domain models.",
        gof_equivalent="State / Visitor",
    ),
    PatternType.INLINE_VALUE_CLASS: PatternDefinition(
        type=PatternType.INLINE_VALUE_CLASS,
        category=PatternCategory.KOTLIN_IDIOMATIC,
        name="Inline Value Class (`@JvmInline value class`)",
        description="Zero-runtime-overhead strongly typed domain primitives preventing primitive obsession.",
        gof_equivalent="Flyweight / Value Object",
    ),
    PatternType.COMPANION_STATIC_FACTORY: PatternDefinition(
        type=PatternType.COMPANION_STATIC_FACTORY,
        category=PatternCategory.KOTLIN_IDIOMATIC,
        name="Companion Object Factory",
        description="Companion object encapsulating static factory creation and named constructors (`invoke`).",
        gof_equivalent="Factory Method",
    ),
    PatternType.OPERATOR_OVERLOADING_DSL: PatternDefinition(
        type=PatternType.OPERATOR_OVERLOADING_DSL,
        category=PatternCategory.KOTLIN_IDIOMATIC,
        name="Operator Overloading DSL",
        description="Custom `operator fun` implementations enabling expressive mathematical and collection DSLs.",
        gof_equivalent="Interpreter",
    ),
    PatternType.SCOPE_FUNCTION_CHAIN: PatternDefinition(
        type=PatternType.SCOPE_FUNCTION_CHAIN,
        category=PatternCategory.KOTLIN_IDIOMATIC,
        name="Scope Function Pipeline (`apply`, `let`, `run`, `also`)",
        description="Idiomatic Kotlin scope functions structuring object initialization and transformation pipelines.",
        gof_equivalent="Builder / Fluent Interface",
    ),

    # 2. Coroutines & Concurrency
    PatternType.STRUCTURED_CONCURRENCY_SCOPE: PatternDefinition(
        type=PatternType.STRUCTURED_CONCURRENCY_SCOPE,
        category=PatternCategory.COROUTINES_CONCURRENCY,
        name="Structured Concurrency (`CoroutineScope` / `coroutineScope`)",
        description="Parent-child lifecycle-bound coroutine scopes preventing unconfined background leaks.",
        gof_equivalent="Async Orchestrator",
    ),
    PatternType.STATEFLOW_REACTIVE_STREAM: PatternDefinition(
        type=PatternType.STATEFLOW_REACTIVE_STREAM,
        category=PatternCategory.COROUTINES_CONCURRENCY,
        name="StateFlow / SharedFlow Reactive Stream",
        description="Hot reactive state stream emitting updates to subscribed collectors in presentation/domain layers.",
        gof_equivalent="Observer",
    ),
    PatternType.CHANNEL_ACTOR_CONCURRENCY: PatternDefinition(
        type=PatternType.CHANNEL_ACTOR_CONCURRENCY,
        category=PatternCategory.COROUTINES_CONCURRENCY,
        name="Channel / Actor Concurrency (`Channel<T>` / `actor`)",
        description="CSP channel-based communication and message-passing actors for thread-safe synchronization.",
        gof_equivalent="Mediator / Active Object",
    ),
    PatternType.SUSPENDING_FUNCTION_ASYNC: PatternDefinition(
        type=PatternType.SUSPENDING_FUNCTION_ASYNC,
        category=PatternCategory.COROUTINES_CONCURRENCY,
        name="Suspending Non-Blocking Function (`suspend fun`)",
        description="Sequential non-blocking asynchronous execution without callback hell.",
        gof_equivalent="Async Command / Continuation",
    ),
    PatternType.DISPATCHER_IO_OFFLOAD: PatternDefinition(
        type=PatternType.DISPATCHER_IO_OFFLOAD,
        category=PatternCategory.COROUTINES_CONCURRENCY,
        name="Thread Affinity Offload (`withContext(Dispatchers.IO)`)",
        description="Explicit switching to background worker pools for blocking I/O and computation.",
        gof_equivalent="Worker Thread / Thread Pool",
    ),

    # 3. Jetpack Compose & Type-Safe DSL
    PatternType.TYPE_SAFE_BUILDER_DSL: PatternDefinition(
        type=PatternType.TYPE_SAFE_BUILDER_DSL,
        category=PatternCategory.COMPOSE_DSL,
        name="Type-Safe Builder DSL (`@DslMarker` / Lambda with Receiver)",
        description="Declarative domain builder using higher-order functions with receivers (`T.() -> Unit`).",
        gof_equivalent="Builder / Interpreter",
    ),
    PatternType.COMPOSE_DECLARATIVE_VIEW: PatternDefinition(
        type=PatternType.COMPOSE_DECLARATIVE_VIEW,
        category=PatternCategory.COMPOSE_DSL,
        name="Compose Declarative View (`@Composable`)",
        description="Declarative UI component transforming data state into reactive UI trees.",
        gof_equivalent="Composite View",
    ),
    PatternType.REMEMBER_MUTABLE_STATE: PatternDefinition(
        type=PatternType.REMEMBER_MUTABLE_STATE,
        category=PatternCategory.COMPOSE_DSL,
        name="Compose State Holder (`remember { mutableStateOf() }`)",
        description="Recomposition-scoped observable state within Jetpack Compose functions.",
        gof_equivalent="Observer / State",
    ),
    PatternType.VIEW_MODEL_STATE_HOLDER: PatternDefinition(
        type=PatternType.VIEW_MODEL_STATE_HOLDER,
        category=PatternCategory.COMPOSE_DSL,
        name="ViewModel State Holder (`ViewModel`)",
        description="Architecture component retaining and coordinating UI state across configuration changes.",
        gof_equivalent="Mediator / Presentation Model",
    ),

    # 4. GoF Creational Patterns
    PatternType.SINGLETON_OBJECT_DECLARATION: PatternDefinition(
        type=PatternType.SINGLETON_OBJECT_DECLARATION,
        category=PatternCategory.CREATIONAL,
        name="Kotlin `object` Singleton",
        description="Thread-safe, lazy language-level Singleton via `object` declaration.",
        gof_equivalent="Singleton",
    ),
    PatternType.FACTORY_METHOD: PatternDefinition(
        type=PatternType.FACTORY_METHOD,
        category=PatternCategory.CREATIONAL,
        name="Factory Method",
        description="Static or interface factory method instantiating polymorphic types (`create...`, `make...`).",
        gof_equivalent="Factory Method",
    ),
    PatternType.ABSTRACT_FACTORY: PatternDefinition(
        type=PatternType.ABSTRACT_FACTORY,
        category=PatternCategory.CREATIONAL,
        name="Abstract Factory",
        description="Factory interface declaring creation methods for families of related objects.",
        gof_equivalent="Abstract Factory",
    ),
    PatternType.BUILDER_FLUENT_CHAIN: PatternDefinition(
        type=PatternType.BUILDER_FLUENT_CHAIN,
        category=PatternCategory.CREATIONAL,
        name="Fluent Builder Chain",
        description="Method chaining builder returning `this` or mutating instance step-by-step.",
        gof_equivalent="Builder",
    ),
    PatternType.PROTOTYPE_DATA_COPY: PatternDefinition(
        type=PatternType.PROTOTYPE_DATA_COPY,
        category=PatternCategory.CREATIONAL,
        name="Prototype Data Copy (`data class copy()`)",
        description="Immutable instance replication and value transformation via `copy()` or `Cloneable`.",
        gof_equivalent="Prototype",
    ),

    # 5. GoF Structural Patterns
    PatternType.ADAPTER_INTERFACE_DELEGATION: PatternDefinition(
        type=PatternType.ADAPTER_INTERFACE_DELEGATION,
        category=PatternCategory.STRUCTURAL,
        name="Adapter via Interface Delegation / Extension",
        description="Adapts third-party or legacy interfaces to domain contracts.",
        gof_equivalent="Adapter",
    ),
    PatternType.BRIDGE_IMPLEMENTOR: PatternDefinition(
        type=PatternType.BRIDGE_IMPLEMENTOR,
        category=PatternCategory.STRUCTURAL,
        name="Bridge Pattern",
        description="Decouples an abstraction hierarchy from its implementation driver/renderer.",
        gof_equivalent="Bridge",
    ),
    PatternType.COMPOSITE_VIEW_TREE: PatternDefinition(
        type=PatternType.COMPOSITE_VIEW_TREE,
        category=PatternCategory.STRUCTURAL,
        name="Composite Component Tree",
        description="Hierarchical composite tree treating individual and grouped elements uniformly.",
        gof_equivalent="Composite",
    ),
    PatternType.DECORATOR_BY_DELEGATION: PatternDefinition(
        type=PatternType.DECORATOR_BY_DELEGATION,
        category=PatternCategory.STRUCTURAL,
        name="Decorator via Class Delegation (`class Foo : Bar by underlying`)",
        description="Kotlin first-class interface delegation forwarding and wrapping method calls.",
        gof_equivalent="Decorator",
    ),
    PatternType.FACADE_COORDINATOR: PatternDefinition(
        type=PatternType.FACADE_COORDINATOR,
        category=PatternCategory.STRUCTURAL,
        name="Facade Coordinator",
        description="Unified coordinator orchestrating multiple subsystem repositories, use cases, or clients.",
        gof_equivalent="Facade",
    ),
    PatternType.FLYWEIGHT_POOL_CACHE: PatternDefinition(
        type=PatternType.FLYWEIGHT_POOL_CACHE,
        category=PatternCategory.STRUCTURAL,
        name="Flyweight Pooling Cache",
        description="Sharing fine-grained immutable instances via factory caching to minimize memory consumption.",
        gof_equivalent="Flyweight",
    ),
    PatternType.PROXY_VIRTUAL_OR_REMOTE: PatternDefinition(
        type=PatternType.PROXY_VIRTUAL_OR_REMOTE,
        category=PatternCategory.STRUCTURAL,
        name="Proxy Pattern",
        description="Surrogate or placeholder object controlling access to an underlying target or remote service.",
        gof_equivalent="Proxy",
    ),

    # 6. GoF Behavioral Patterns
    PatternType.CHAIN_OF_RESPONSIBILITY: PatternDefinition(
        type=PatternType.CHAIN_OF_RESPONSIBILITY,
        category=PatternCategory.BEHAVIORAL,
        name="Chain of Responsibility",
        description="Sequence of interceptor/handler objects passing requests along a handler chain.",
        gof_equivalent="Chain of Responsibility",
    ),
    PatternType.COMMAND_ACTION_OBJECT: PatternDefinition(
        type=PatternType.COMMAND_ACTION_OBJECT,
        category=PatternCategory.BEHAVIORAL,
        name="Command Action Object",
        description="Encapsulates an operation, its receiver, and parameters into an executable command.",
        gof_equivalent="Command",
    ),
    PatternType.INTERPRETER_EXPRESSION_AST: PatternDefinition(
        type=PatternType.INTERPRETER_EXPRESSION_AST,
        category=PatternCategory.BEHAVIORAL,
        name="Interpreter Pattern (Expression AST)",
        description="Evaluates domain sentences or language grammars through composite expression trees.",
        gof_equivalent="Interpreter",
    ),
    PatternType.ITERATOR_SEQUENCE_FLOW: PatternDefinition(
        type=PatternType.ITERATOR_SEQUENCE_FLOW,
        category=PatternCategory.BEHAVIORAL,
        name="Iterator / Sequence / Flow Traversal",
        description="Lazy sequential element traversal conforming to `Sequence<T>`, `Iterator<T>`, or `Flow<T>`.",
        gof_equivalent="Iterator",
    ),
    PatternType.MEDIATOR_COORDINATOR: PatternDefinition(
        type=PatternType.MEDIATOR_COORDINATOR,
        category=PatternCategory.BEHAVIORAL,
        name="Mediator / Flow Coordinator",
        description="Centralized coordinator decoupling components and managing communication flows.",
        gof_equivalent="Mediator",
    ),
    PatternType.MEMENTO_SERIALIZABLE_STATE: PatternDefinition(
        type=PatternType.MEMENTO_SERIALIZABLE_STATE,
        category=PatternCategory.BEHAVIORAL,
        name="Serializable Memento Snapshot",
        description="Captures and externalizes object state as a `@Serializable` or Parcelable snapshot.",
        gof_equivalent="Memento",
    ),
    PatternType.OBSERVER_FLOW_PUBLISHED: PatternDefinition(
        type=PatternType.OBSERVER_FLOW_PUBLISHED,
        category=PatternCategory.BEHAVIORAL,
        name="Flow / LiveData Observer",
        description="Reactive observer publisher notifying subscribed collectors on state mutations.",
        gof_equivalent="Observer",
    ),
    PatternType.STATE_SEALED_CLASS_FSM: PatternDefinition(
        type=PatternType.STATE_SEALED_CLASS_FSM,
        category=PatternCategory.BEHAVIORAL,
        name="Sealed Class State Machine",
        description="Type-safe finite state machine modeling distinct lifecycle states with payload data.",
        gof_equivalent="State",
    ),
    PatternType.STRATEGY_LAMBDA_INJECTION: PatternDefinition(
        type=PatternType.STRATEGY_LAMBDA_INJECTION,
        category=PatternCategory.BEHAVIORAL,
        name="Strategy Interface / Lambda Injection",
        description="Interchangeable algorithm strategy encapsulated in functional interface or lambda property.",
        gof_equivalent="Strategy",
    ),
    PatternType.TEMPLATE_METHOD_ALGORITHM: PatternDefinition(
        type=PatternType.TEMPLATE_METHOD_ALGORITHM,
        category=PatternCategory.BEHAVIORAL,
        name="Template Method Algorithm Skeleton",
        description="Defines algorithm skeleton in abstract class or interface default method with step hooks.",
        gof_equivalent="Template Method",
    ),
    PatternType.VISITOR_SEALED_WHEN: PatternDefinition(
        type=PatternType.VISITOR_SEALED_WHEN,
        category=PatternCategory.BEHAVIORAL,
        name="Visitor Double Dispatch / Exhaustive `when`",
        description="Operations over sealed type structures via double dispatch or exhaustive `when` expressions.",
        gof_equivalent="Visitor",
    ),

    # 7. Resilience, Safety & Hazards
    PatternType.GLOBALSCOPE_COROUTINE_LEAK: PatternDefinition(
        type=PatternType.GLOBALSCOPE_COROUTINE_LEAK,
        category=PatternCategory.RESILIENCE,
        name="GlobalScope Coroutine Leak Hazard",
        description="Launching coroutines in `GlobalScope` unconfined from component lifecycle, causing memory and execution leaks.",
        recommendation="Use structured lifecycle scopes (`viewModelScope`, `lifecycleScope`, `coroutineScope`).",
    ),
    PatternType.NON_CANCELLATION_EXCEPTION_SWALLOW: PatternDefinition(
        type=PatternType.NON_CANCELLATION_EXCEPTION_SWALLOW,
        category=PatternCategory.RESILIENCE,
        name="Swallowed CancellationException Hazard",
        description="Catching generic `Exception` inside coroutines without rethrowing `CancellationException`, breaking cancellation.",
        recommendation="Rethrow `CancellationException` or catch specific domain exceptions.",
    ),
    PatternType.FORCE_NULL_ASSERTION_HAZARD: PatternDefinition(
        type=PatternType.FORCE_NULL_ASSERTION_HAZARD,
        category=PatternCategory.RESILIENCE,
        name="Unsafe Force-Null Assertion (`!!`) Hazard",
        description="Force-null unwrapping with `!!` risking immediate `NullPointerException` at runtime.",
        recommendation="Use safe call operators (`?.`), Elvis (`?:`), or `let` blocks.",
    ),
    PatternType.FORCE_CAST_HAZARD: PatternDefinition(
        type=PatternType.FORCE_CAST_HAZARD,
        category=PatternCategory.RESILIENCE,
        name="Unsafe Force-Cast (`as`) Hazard",
        description="Unsafe type casting with `as` instead of safe cast `as?`, risking `ClassCastException`.",
        recommendation="Use safe downcasting (`as?`) with fallback handling.",
    ),
    PatternType.MAIN_THREAD_BLOCKING_CALL: PatternDefinition(
        type=PatternType.MAIN_THREAD_BLOCKING_CALL,
        category=PatternCategory.RESILIENCE,
        name="Main Thread Blocking Call (`Thread.sleep` / `runBlocking`)",
        description="Executing blocking operations on the Main UI thread causing ANR (Application Not Responding).",
        recommendation="Offload blocking calls with `withContext(Dispatchers.IO)`.",
    ),
    PatternType.STRONG_CONTEXT_LEAK: PatternDefinition(
        type=PatternType.STRONG_CONTEXT_LEAK,
        category=PatternCategory.RESILIENCE,
        name="Android Context / Activity Memory Leak",
        description="Retaining strong references to Android `Activity` or `Context` in static/singleton scope.",
        recommendation="Use `ApplicationContext` or `WeakReference<Activity>`.",
    ),

    # 8. SOLID & Clean Architecture Principles
    PatternType.MASSIVE_VIEWMODEL_SRP: PatternDefinition(
        type=PatternType.MASSIVE_VIEWMODEL_SRP,
        category=PatternCategory.PRINCIPLE,
        name="SRP Violation: Massive ViewModel / God Class",
        description="Type with excessive responsibilities, methods, or lines of code violating SRP.",
        recommendation="Decompose into focused UseCases and Domain Services.",
    ),
    PatternType.FAT_INTERFACE_ISP: PatternDefinition(
        type=PatternType.FAT_INTERFACE_ISP,
        category=PatternCategory.PRINCIPLE,
        name="ISP Violation: Fat Interface",
        description="Interface declaring too many required methods, forcing implementors to depend on unused methods.",
        recommendation="Split into smaller role-based interfaces.",
    ),
    PatternType.DYNAMIC_CAST_WHEN_CASCADE_OCP: PatternDefinition(
        type=PatternType.DYNAMIC_CAST_WHEN_CASCADE_OCP,
        category=PatternCategory.PRINCIPLE,
        name="OCP Violation: Typecheck When/Is Cascade",
        description="Repeated `when (x is A)` type checking cascades requiring modification for new types.",
        recommendation="Replace with polymorphic dispatch.",
    ),
    PatternType.KISS_CYCLOMATIC_COMPLEXITY: PatternDefinition(
        type=PatternType.KISS_CYCLOMATIC_COMPLEXITY,
        category=PatternCategory.PRINCIPLE,
        name="KISS Violation: High Cyclomatic Complexity",
        description="Function containing excessive decision points (> 8 branches), violating KISS.",
        recommendation="Refactor into smaller helper functions or lookup tables.",
    ),
    PatternType.KISS_LONG_PARAMETER_LIST: PatternDefinition(
        type=PatternType.KISS_LONG_PARAMETER_LIST,
        category=PatternCategory.PRINCIPLE,
        name="KISS Violation: Long Parameter List",
        description="Function or constructor accepting >= 5 parameters.",
        recommendation="Bundle into a Parameter Object / Data Class.",
    ),
    PatternType.DRY_DUPLICATE_LOGIC: PatternDefinition(
        type=PatternType.DRY_DUPLICATE_LOGIC,
        category=PatternCategory.PRINCIPLE,
        name="DRY Violation: Duplicate Code Logic",
        description="Duplicated algorithmic sequences across multiple functions or classes.",
        recommendation="Extract common logic into reusable extension or utility functions.",
    ),
    PatternType.DEMETER_LAW_TRAIN_WRECK: PatternDefinition(
        type=PatternType.DEMETER_LAW_TRAIN_WRECK,
        category=PatternCategory.PRINCIPLE,
        name="Law of Demeter Violation (Train Wreck)",
        description="Deep navigation across indirect object graphs (`a.b.c.d.e`), increasing coupling.",
        recommendation="Follow 'Tell, Don't Ask' principle and add direct delegate methods.",
    ),
}
