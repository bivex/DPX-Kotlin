# 🎯 DPX-Kotlin: Architectural Context & Pattern Report

- **Target Project:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture`
- **Scanned Files:** 6
- **Total Detections:** 20
- **Scan Time:** 0.001s

## 📊 Summary by Category

| Category | Detections |
|---|:---:|
| `coroutines_concurrency` | 9 |
| `compose_dsl` | 4 |
| `creational` | 3 |
| `kotlin_idiomatic` | 2 |
| `behavioral` | 2 |

## 🔍 Detailed Pattern Instances & Violations

### 1. sealed_hierarchy_adt on `UserUiState` (95% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/domain/UserAccount.kt:16:1`
- **Summary:** Exhaustive sum types / Algebraic Data Types representing closed polymorphic domain models.
- **Evidence Trail:**
  - `+95%` (KOTLIN_SEALED_HIERARCHY): Sealed type 'UserUiState' (sealed_interface) defines an Algebraic Data Type (ADT) hierarchy for exhaustive pattern matching

### 2. inline_value_class on `UserId` (95% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `value_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/domain/UserAccount.kt:6:1`
- **Summary:** Zero-runtime-overhead strongly typed domain primitives preventing primitive obsession.
- **Evidence Trail:**
  - `+95%` (KOTLIN_INLINE_VALUE_CLASS): Value class 'UserId' encapsulates strongly typed domain primitive with zero runtime allocation overhead

### 3. structured_concurrency_scope on `UserViewModel` (90% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/presentation/UserViewModel.kt:12:1`
- **Summary:** Parent-child lifecycle-bound coroutine scopes preventing unconfined background leaks.
- **Evidence Trail:**
  - `+90%` (COROUTINES_STRUCTURED_SCOPE): Type 'UserViewModel' bounds asynchronous jobs within structured CoroutineScope

### 4. stateflow_reactive_stream on `UserRepositoryImpl` (95% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/data/UserRepositoryImpl.kt:12:1`
- **Summary:** Hot reactive state stream emitting updates to subscribed collectors in presentation/domain layers.
- **Evidence Trail:**
  - `+95%` (COROUTINES_STATEFLOW_STREAM): Type 'UserRepositoryImpl' defines 1 hot StateFlow/SharedFlow reactive stream(s) (_usersFlow)

### 5. stateflow_reactive_stream on `UserViewModel` (95% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/presentation/UserViewModel.kt:12:1`
- **Summary:** Hot reactive state stream emitting updates to subscribed collectors in presentation/domain layers.
- **Evidence Trail:**
  - `+95%` (COROUTINES_STATEFLOW_STREAM): Type 'UserViewModel' defines 2 hot StateFlow/SharedFlow reactive stream(s) (_uiState, uiState)

### 6. suspending_function_async on `getUser` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/data/UserRepositoryImpl.kt:15:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getUser' enables non-blocking asynchronous continuation

### 7. suspending_function_async on `saveUser` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/data/UserRepositoryImpl.kt:19:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'saveUser' enables non-blocking asynchronous continuation

### 8. suspending_function_async on `getUser` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/domain/UserRepository.kt:6:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getUser' enables non-blocking asynchronous continuation

### 9. suspending_function_async on `saveUser` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/domain/UserRepository.kt:7:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'saveUser' enables non-blocking asynchronous continuation

### 10. dispatcher_io_offload on `getUser` (90% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/data/UserRepositoryImpl.kt:15:1`
- **Summary:** Explicit switching to background worker pools for blocking I/O and computation.
- **Evidence Trail:**
  - `+90%` (COROUTINES_DISPATCHER_OFFLOAD): Function 'getUser' explicitly offloads blocking computation using withContext(Dispatchers)

### 11. dispatcher_io_offload on `saveUser` (90% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/data/UserRepositoryImpl.kt:19:1`
- **Summary:** Explicit switching to background worker pools for blocking I/O and computation.
- **Evidence Trail:**
  - `+90%` (COROUTINES_DISPATCHER_OFFLOAD): Function 'saveUser' explicitly offloads blocking computation using withContext(Dispatchers)

### 12. compose_declarative_view on `UserProfileScreen` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/presentation/UserScreen.kt:9:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'UserProfileScreen' acts as a declarative UI component

### 13. compose_declarative_view on `UserCardView` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/presentation/UserScreen.kt:15:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'UserCardView' acts as a declarative UI component

### 14. remember_mutable_state on `UserProfileScreen` (90% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/presentation/UserScreen.kt:9:1`
- **Summary:** Recomposition-scoped observable state within Jetpack Compose functions.
- **Evidence Trail:**
  - `+90%` (COMPOSE_REMEMBER_MUTABLE_STATE): Function 'UserProfileScreen' preserves observable UI state across recompositions using remember

### 15. view_model_state_holder on `UserViewModel` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/presentation/UserViewModel.kt:12:1`
- **Summary:** Architecture component retaining and coordinating UI state across configuration changes.
- **Evidence Trail:**
  - `+95%` (COMPOSE_VIEWMODEL_STATE_HOLDER): Class 'UserViewModel' implements ViewModel architectural state holder

### 16. singleton_object_declaration on `NetworkConfig` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/data/NetworkConfig.kt:3:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'NetworkConfig' provides language-level thread-safe Singleton

### 17. factory_method on `Companion.createClient` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/data/NetworkConfig.kt:9:1`
- **Summary:** Static or interface factory method instantiating polymorphic types (`create...`, `make...`).
- **Evidence Trail:**
  - `+85%` (CREATIONAL_FACTORY_METHOD): Method 'createClient' on 'Companion' encapsulates instance instantiation as a Factory Method

### 18. prototype_data_copy on `UserAccount` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/domain/UserAccount.kt:9:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'UserAccount' implements Prototype pattern for instance replication and value transformation

### 19. observer_flow_published on `UserViewModel` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/presentation/UserViewModel.kt:12:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'UserViewModel' acts as Reactive Observer Subject publishing 1 stream(s)

### 20. state_sealed_class_fsm on `UserUiState` (95% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/examples/clean_android_architecture/domain/UserAccount.kt:16:1`
- **Summary:** Type-safe finite state machine modeling distinct lifecycle states with payload data.
- **Evidence Trail:**
  - `+95%` (BEHAVIORAL_STATE_SEALED_FSM): Sealed type 'UserUiState' models type-safe Finite State Machine (FSM) with associated lifecycle states
