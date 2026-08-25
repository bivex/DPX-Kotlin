# 🎯 DPX-Kotlin: Coroutines, Flow, Jetpack Compose, GoF & Multiplatform Architectural Pattern Detector

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Kotlin Version](https://img.shields.io/badge/Kotlin-1.8%20--%202.0+-7F52FF?logo=kotlin&logoColor=white)](https://kotlinlang.org/)
[![Python: 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Architecture: Hexagonal DDD](https://img.shields.io/badge/Architecture-Hexagonal%20DDD-blueviolet)](https://alistair.cockburn.us/hexagonal-architecture/)
[![CLI: Typer & Rich](https://img.shields.io/badge/CLI-Typer%20%26%20Rich-009688)](https://typer.tiangolo.com)
[![SARIF OASIS v2.1.0](https://img.shields.io/badge/SARIF-OASIS%20v2.1.0-blue)](https://sarifweb.azurewebsites.net)

**DPX-Kotlin** is an enterprise-grade static analysis engine and architectural pattern detector for Kotlin codebases. Designed for **Android, Kotlin Multiplatform (KMP), Compose Multiplatform, and Backend (Ktor, Spring Boot)**, it analyzes **Kotlin Idioms (Extension Functions, Delegated Properties, Sealed ADTs, Inline Classes)**, **Structured Concurrency (Coroutines, StateFlow, Channels)**, **Jetpack Compose DSLs**, **all 23 GoF Design Patterns**, and **Android/Coroutines Safety Hazards (GlobalScope leaks, swallowed CancellationException, force nulls)**.

[Features](#-key-features) • [Installation](#-installation) • [CLI Usage](#-cli-usage) • [Supported Rules](#-supported-pattern-rules--checks) • [The DPX Suite Family](#-the-dpx-suite-family)

</div>

---

## 🌟 Key Features

- 🧬 **Kotlin Idiomatic & Multiplatform Patterns:** Detects extension functions/properties, delegated properties (`by lazy`, `by Delegates.observable`, custom delegates), sealed class/interface ADTs, `@JvmInline value class` primitives, companion static factories, and scope pipelines (`apply`, `let`, `run`, `also`).
- ⚡ **Structured Concurrency & Coroutines:** Full inspection of `CoroutineScope`, `coroutineScope`, hot reactive state streams (`StateFlow`, `SharedFlow`), CSP channels (`Channel<T>`), non-blocking `suspend fun`, and thread-affinity offloading (`withContext(Dispatchers.IO)`).
- 🎨 **Jetpack Compose & Type-Safe DSLs:** Audits type-safe builders (`@DslMarker` with lambda receivers `T.() -> Unit`), `@Composable` declarative view components, `remember { mutableStateOf() }`, and `ViewModel` state holders.
- 🏛️ **100% Complete Gang of Four (GoF 23/23):** Comprehensive detection of all 23 classic Creational, Structural, and Behavioral patterns expressed through modern idiomatic Kotlin features (class delegation `by`, data class `copy()`, sealed `when`, `object` singletons).
- 🛡️ **Android & Coroutines Safety Auditing:** Detects `GlobalScope` lifecycle leaks, generic exception catching that swallows `CancellationException`, force-null assertions (`!!`), unsafe downcasting (`as`), and Main UI thread blocking (`Thread.sleep`, `runBlocking`).
- 📊 **Interactive Architecture Observability HUD:** Zero-dependency interactive HTML dashboard with instant search, KPI breakdown, and built-in **`🤖 Copy AI Context Prompt`** generator for LLMs (Claude, GPT-4, Gemini).
- 🔒 **CI/CD & GitHub Security Ready:** Standardized **OASIS SARIF v2.1.0**, JSON, and Markdown reports.

---

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/bivex/DPX-Kotlin.git
cd DPX-Kotlin

# Install dependencies using uv or pip
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

---

## 💻 CLI Usage

### 1. Scan a Kotlin Project or Android App
```bash
# Terminal scan with Rich formatting
dpx-kotlin scan /path/to/android/project

# Generate interactive HTML HUD Dashboard
dpx-kotlin scan /path/to/android/project -H reports/kotlin_hud.html

# Generate AI Context Prompt for LLMs
dpx-kotlin scan /path/to/android/project --llm

# Filter for specific coroutines or safety patterns
dpx-kotlin scan /path/to/android/project -p structured_concurrency_scope -p globalscope_coroutine_leak

# Export SARIF for GitHub Code Scanning
dpx-kotlin scan /path/to/android/project -S reports/results.sarif
```

### 2. Inspect Supported Architectural Rules
```bash
dpx-kotlin rules
```

### 3. Query Deep Pattern Documentation
```bash
dpx-kotlin info structured_concurrency_scope
dpx-kotlin info globalscope_coroutine_leak
```

---

## 📋 Supported Pattern Rules & Checks

### 1. 🧬 Kotlin Idiomatic Patterns
- `extension_function_adapter`: Retroactive API adaptation without subclassing.
- `delegated_property_lazy`: Property behavior delegation (`by lazy`, `by viewModels()`).
- `sealed_hierarchy_adt`: Exhaustive Algebraic Data Types for domain modeling.
- `inline_value_class`: `@JvmInline value class` zero-allocation primitives.
- `companion_static_factory`: Static factory creation in `companion object`.
- `operator_overloading_dsl`: Domain expression operator overloading (`operator fun`).
- `scope_function_chain`: Object lifecycle pipelines (`apply`, `also`, `let`, `run`).

### 2. ⚡ Coroutines & Structured Concurrency
- `structured_concurrency_scope`: Lifecycle-bound parent-child `CoroutineScope`.
- `stateflow_reactive_stream`: Hot reactive state streams (`StateFlow`, `SharedFlow`).
- `channel_actor_concurrency`: CSP channel communication and message-passing.
- `suspending_function_async`: Non-blocking sequential asynchronous `suspend fun`.
- `dispatcher_io_offload`: Thread-affinity offloading via `withContext(Dispatchers.IO)`.

### 3. 🎨 Jetpack Compose & Type-Safe DSL
- `type_safe_builder_dsl`: Declarative DSL builders using lambda with receiver (`T.() -> Unit`).
- `compose_declarative_view`: `@Composable` declarative UI tree components.
- `remember_mutable_state`: Preserving observable state across recompositions (`remember`).
- `view_model_state_holder`: Android `ViewModel` coordinating state across configuration changes.

### 4. 🏛️ GoF Creational Patterns (5/5)
- `singleton_object_declaration`: Thread-safe language-level `object` Singleton.
- `factory_method`: Static / polymorphic factory methods (`create...`, `make...`).
- `abstract_factory`: Factory interfaces declaring families of creation methods.
- `builder_fluent_chain`: Fluent chaining returning `this` / mutating instances.
- `prototype_data_copy`: Instance replication via `data class copy()` / `Cloneable`.

### 5. 🧱 GoF Structural Patterns (7/7)
- `adapter_interface_delegation`: Adapting target interfaces to domain contracts.
- `bridge_implementor`: Decoupling abstraction from implementor protocols.
- `composite_view_tree`: Recursive component and view tree hierarchies.
- `decorator_by_delegation`: Class interface delegation (`class Foo : Bar by underlying`).
- `facade_coordinator`: Unified coordinator orchestrating subsystem services/use cases.
- `flyweight_pool_cache`: Fine-grained instance sharing via factory caching.
- `proxy_virtual_or_remote`: Surrogate proxy controlling access to target services.

### 6. 🎯 GoF Behavioral Patterns (11/11)
- `chain_of_responsibility`: Linked handlers delegating requests along a chain.
- `command_action_object`: Command objects with `execute()` / `invoke()`.
- `interpreter_expression_ast`: Domain expression AST evaluation (`interpret()`).
- `iterator_sequence_flow`: Lazy traversal over `Sequence`, `Iterator`, or `Flow`.
- `mediator_coordinator`: App and navigation flow coordinators.
- `memento_serializable_state`: State snapshots via `@Serializable` / `Parcelable`.
- `observer_flow_published`: Reactive Flow / LiveData state publishing.
- `state_sealed_class_fsm`: Type-safe Enum / Sealed Class state machines.
- `strategy_lambda_injection`: Interchangeable algorithm strategy injection.
- `template_method_algorithm`: Algorithm skeletons with lifecycle step hooks.
- `visitor_sealed_when`: Double dispatch / exhaustive `when` over sealed types.

### 7. 🛡️ Resilience, Android & Coroutines Hazards
- `globalscope_coroutine_leak`: Coroutines launched in `GlobalScope` escaping lifecycles.
- `non_cancellation_exception_swallow`: Catching generic `Exception` without rethrowing `CancellationException`.
- `force_null_assertion_hazard`: Unsafe force-null assertion (`!!`) risking `NullPointerException`.
- `force_cast_hazard`: Unsafe downcasting (`as ` without `as?`) risking `ClassCastException`.
- `main_thread_blocking_call`: Synchronous blocking calls (`Thread.sleep`, `runBlocking`) on UI thread.
- `strong_context_leak`: Retaining Android `Activity` or `Context` in static/companion scope.

### 8. 📐 SOLID & Code Quality Principles
- `massive_viewmodel_srp`: Massive ViewModel / God Class SRP violations.
- `fat_interface_isp`: Fat interfaces declaring too many required methods.
- `dynamic_cast_when_cascade_ocp`: Typecheck `when (x is ...)` cascades violating OCP.
- `kiss_cyclomatic_complexity`: High cyclomatic complexity (> 8 branch points).
- `kiss_long_parameter_list`: Functions with excessive parameters (>= 5).
- `dry_duplicate_logic`: Duplicated algorithmic logic across methods.
- `demeter_law_train_wreck`: Law of Demeter deep dot-chain navigation (`a.b.c.d.e`).

---

## 🌐 The DPX Suite Family

Cross-language architectural static analysis across all modern programming languages:

| Repository | Language / Ecosystem | Primary Paradigms & Focus |
|---|---|---|
| **[`DPX-Mojo`](https://github.com/bivex/DPX-Mojo)** | **Mojo** (24.x - 25.x+) | **SIMD Vectorization, Ownership, Memory Safety, GoF 23, AI Acceleration** |
| **[`DPX-Julia`](https://github.com/bivex/DPX-Julia)** | **Julia** (1.6 - 1.11+) | **Multiple Dispatch, Holy Traits, Metaprogramming, Tasks, GoF 23** |
| **[`DPX-Kotlin`](https://github.com/bivex/DPX-Kotlin)** | **Kotlin** (1.8 - 2.0+) | **Coroutines, Flow, Jetpack Compose, Multiplatform, GoF 23** |
| **[`DPX-Swift`](https://github.com/bivex/DPX-Swift)** | **Swift** (5.5 - 6.0+) | **Protocol-Oriented, Actor Concurrency, SwiftUI, ARC Safety** |
| **[`DPX-CSharp`](https://github.com/bivex/DPX-CSharp)** | **C#** (10 - 13 / .NET 8-9) | **Clean Architecture, CQRS MediatR, Channel Pipelines** |
| **[`DPX-TypeScript`](https://github.com/bivex/DPX-TypeScript)** | **TypeScript / JavaScript** | **Hexagonal DI, Decorator Meta, Reactive Streams, React/NestJS** |
| **[`DPX-Rust`](https://github.com/bivex/DPX-Rust)** | **Rust** (Edition 2021/2024) | **Zero-Cost Abstractions, RAII Lifetimes, Typestate Pattern** |
| **[`DPX-Go`](https://github.com/bivex/DPX-Go)** | **Go** (1.18 - 1.24+) | **Goroutine Channels, CSP Concurrency, Pipeline Streaming** |
| **[`DPX-Py`](https://github.com/bivex/DPX-Py)** | **Python** (3.8 - 3.13+) | **Multi-Paradigm Hexagonal, Data Flow Engine, AsyncIO** |
| **[`DPX-Php`](https://github.com/bivex/DPX-Php)** | **PHP** (8.1 - 8.4+) | **Attribute-driven DDD, Fiber Concurrency, Laravel/Symfony** |
| **[`DPX-Haskell`](https://github.com/bivex/DPX-Haskell)** | **Haskell** (GHC 9.2 - 9.12+) | **Category Theory, Monad Transformers, Free Monads, Optics** |
| **[`DPX-OCaml`](https://github.com/bivex/DPX-OCaml)** | **OCaml** (4.14 - 5.3+ Multicore) | **Functor Modules, Effect Handlers, GADTs, Railway Monads** |
| **[`DPX-Elixir`](https://github.com/bivex/DPX-Elixir)** | **Elixir** (OTP 25 - 27+) | **GenServer, DynamicSupervisor, Actor Fault Tolerance** |
| **[`DPX-Erlang`](https://github.com/bivex/DPX-Erlang)** | **Erlang/OTP** (24 - 27+) | **OTP Behaviors, Supervision Trees, Message Passing** |
| **[`DPX-C`](https://github.com/bivex/DPX-C)** | **C** (C99 - C23) | **Opaque Structs, VTables, MISRA/CERT Safety, Arena Allocators** |
| **[`DPX-Cpp`](https://github.com/bivex/DPX-Cpp)** | **C++** (C++14 - C++20) | **CRTP, Policy-Based Design, RAII Memory Safety, ANTLR4 AST** |
| **[`DPX-Java`](https://github.com/bivex/DPX-Java)** | **Java** (17 - 23+) | **Virtual Threads, Spring Boot / Jakarta EE, GoF Patterns** |
| **[`DPX`](https://github.com/bivex/DPX)** | **Clojure** / Meta Engine | **Pure Functional, Multimethods, Homoiconic Macro Architecture** |
 **Julia** (1.6 - 1.11+) | **Multiple Dispatch, Holy Traits, Metaprogramming, Tasks, GoF 23** |
| **[`DPX-Kotlin`](https://github.com/bivex/DPX-Kotlin)** | **Kotlin** (1.8 - 2.0+) | **Coroutines, Flow, Jetpack Compose, Multiplatform, GoF 23** |
| **[`DPX-Swift`](https://github.com/bivex/DPX-Swift)** | **Swift** (5.5 - 6.0+) | **Protocol-Oriented, Actor Concurrency, SwiftUI, ARC Safety** |
| **[`DPX-CSharp`](https://github.com/bivex/DPX-CSharp)** | **C#** (10 - 13 / .NET 8-9) | **Clean Architecture, CQRS MediatR, Channel Pipelines** |
| **[`DPX-TypeScript`](https://github.com/bivex/DPX-TypeScript)** | **TypeScript / JavaScript** | **Hexagonal DI, Decorator Meta, Reactive Streams, React/NestJS** |
| **[`DPX-Rust`](https://github.com/bivex/DPX-Rust)** | **Rust** (Edition 2021/2024) | **Zero-Cost Abstractions, RAII Lifetimes, Typestate Pattern** |
| **[`DPX-Go`](https://github.com/bivex/DPX-Go)** | **Go** (1.18 - 1.24+) | **Goroutine Channels, CSP Concurrency, Pipeline Streaming** |
| **[`DPX-Py`](https://github.com/bivex/DPX-Py)** | **Python** (3.8 - 3.13+) | **Multi-Paradigm Hexagonal, Data Flow Engine, AsyncIO** |
| **[`DPX-Php`](https://github.com/bivex/DPX-Php)** | **PHP** (8.1 - 8.4+) | **Attribute-driven DDD, Fiber Concurrency, Laravel/Symfony** |
| **[`DPX-Haskell`](https://github.com/bivex/DPX-Haskell)** | **Haskell** (GHC 9.2 - 9.12+) | **Category Theory, Monad Transformers, Free Monads, Optics** |
| **[`DPX-OCaml`](https://github.com/bivex/DPX-OCaml)** | **OCaml** (4.14 - 5.3+ Multicore) | **Functor Modules, Effect Handlers, GADTs, Railway Monads** |
| **[`DPX-Elixir`](https://github.com/bivex/DPX-Elixir)** | **Elixir** (OTP 25 - 27+) | **GenServer, DynamicSupervisor, Actor Fault Tolerance** |
| **[`DPX-Erlang`](https://github.com/bivex/DPX-Erlang)** | **Erlang/OTP** (24 - 27+) | **OTP Behaviors, Supervision Trees, Message Passing** |
| **[`DPX-C`](https://github.com/bivex/DPX-C)** | **C** (C99 - C23) | **Opaque Structs, VTables, MISRA/CERT Safety, Arena Allocators** |
| **[`DPX-Cpp`](https://github.com/bivex/DPX-Cpp)** | **C++** (C++14 - C++20) | **CRTP, Policy-Based Design, RAII Memory Safety, ANTLR4 AST** |
| **[`DPX-Java`](https://github.com/bivex/DPX-Java)** | **Java** (17 - 23+) | **Virtual Threads, Spring Boot / Jakarta EE, GoF Patterns** |
| **[`DPX`](https://github.com/bivex/DPX)** | **Clojure** / Meta Engine | **Pure Functional, Multimethods, Homoiconic Macro Architecture** |

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
