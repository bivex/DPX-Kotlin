# 🎯 DPX-Kotlin: Architectural Context & Pattern Report

- **Target Project:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid`
- **Scanned Files:** 350
- **Total Detections:** 512
- **Scan Time:** 0.081s

## 📊 Summary by Category

| Category | Detections |
|---|:---:|
| `kotlin_idiomatic` | 165 |
| `coroutines_concurrency` | 131 |
| `compose_dsl` | 85 |
| `creational` | 66 |
| `behavioral` | 26 |
| `principle` | 19 |
| `structural` | 13 |
| `resilience` | 7 |

## 🔍 Detailed Pattern Instances & Violations

### 1. extension_function_adapter on `JavaContext.isAndroidTest` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/lint/src/main/kotlin/com/google/samples/apps/nowinandroid/lint/TestMethodNameDetector.kt:58:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'JavaContext.isAndroidTest' retroactively augments type without subclassing

### 2. extension_function_adapter on `AnalyticsHelper.logScreenView` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/AnalyticsExtensions.kt:31:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'AnalyticsHelper.logScreenView' retroactively augments type without subclassing

### 3. extension_function_adapter on `AnalyticsHelper.logNewsResourceOpened` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/AnalyticsExtensions.kt:42:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'AnalyticsHelper.logNewsResourceOpened' retroactively augments type without subclassing

### 4. extension_function_adapter on `PopulatedNewsResource.asExternalModel` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/model/PopulatedNewsResource.kt:42:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'PopulatedNewsResource.asExternalModel' retroactively augments type without subclassing

### 5. extension_function_adapter on `PopulatedNewsResource.asFtsEntity` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/model/PopulatedNewsResource.kt:53:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'PopulatedNewsResource.asFtsEntity' retroactively augments type without subclassing

### 6. extension_function_adapter on `TopicEntity.asExternalModel` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/model/TopicEntity.kt:44:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'TopicEntity.asExternalModel' retroactively augments type without subclassing

### 7. extension_function_adapter on `NewsResourceEntity.asExternalModel` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/model/NewsResourceEntity.kt:44:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'NewsResourceEntity.asExternalModel' retroactively augments type without subclassing

### 8. extension_function_adapter on `TopicEntity.asFtsEntity` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/model/TopicFtsEntity.kt:43:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'TopicEntity.asFtsEntity' retroactively augments type without subclassing

### 9. extension_function_adapter on `Orientation.valueOf` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/Scrollbar.kt:165:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Orientation.valueOf' retroactively augments type without subclassing

### 10. extension_function_adapter on `Orientation.valueOf` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/Scrollbar.kt:173:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Orientation.valueOf' retroactively augments type without subclassing

### 11. extension_function_adapter on `Orientation.valueOf` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/Scrollbar.kt:181:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Orientation.valueOf' retroactively augments type without subclassing

### 12. extension_function_adapter on `ContentDrawScope.draw` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/AppScrollbars.kt:196:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'ContentDrawScope.draw' retroactively augments type without subclassing

### 13. extension_function_adapter on `List<T>.floatSumOf` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/ScrollbarExt.kt:233:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'List<T>.floatSumOf' retroactively augments type without subclassing

### 14. extension_function_adapter on `NetworkTopic.asExternalModel` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/model/NetworkTopic.kt:36:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'NetworkTopic.asExternalModel' retroactively augments type without subclassing

### 15. extension_function_adapter on `Flow<T>.asResult` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/common/src/main/kotlin/com/google/samples/apps/nowinandroid/core/common/result/Result.kt:30:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Flow<T>.asResult' retroactively augments type without subclassing

### 16. extension_function_adapter on `List<NewsResource>.mapToUserNewsResources` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/model/src/main/kotlin/com/google/samples/apps/nowinandroid/core/model/data/UserNewsResource.kt:56:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'List<NewsResource>.mapToUserNewsResources' retroactively augments type without subclassing

### 17. extension_function_adapter on `List<NetworkChangeList>.after` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/test/kotlin/com/google/samples/apps/nowinandroid/core/data/testdoubles/TestNiaNetworkDataSource.kt:94:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'List<NetworkChangeList>.after' retroactively augments type without subclassing

### 18. extension_function_adapter on `Syncable.sync` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/SyncUtilities.kt:36:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Syncable.sync' retroactively augments type without subclassing

### 19. extension_function_adapter on `AnalyticsHelper.logNewsResourceBookmarkToggled` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/AnalyticsExtensions.kt:23:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'AnalyticsHelper.logNewsResourceBookmarkToggled' retroactively augments type without subclassing

### 20. extension_function_adapter on `AnalyticsHelper.logTopicFollowToggled` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/AnalyticsExtensions.kt:36:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'AnalyticsHelper.logTopicFollowToggled' retroactively augments type without subclassing

### 21. extension_function_adapter on `AnalyticsHelper.logThemeChanged` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/AnalyticsExtensions.kt:49:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'AnalyticsHelper.logThemeChanged' retroactively augments type without subclassing

### 22. extension_function_adapter on `AnalyticsHelper.logDarkThemeConfigChanged` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/AnalyticsExtensions.kt:59:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'AnalyticsHelper.logDarkThemeConfigChanged' retroactively augments type without subclassing

### 23. extension_function_adapter on `AnalyticsHelper.logDynamicColorPreferenceChanged` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/AnalyticsExtensions.kt:69:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'AnalyticsHelper.logDynamicColorPreferenceChanged' retroactively augments type without subclassing

### 24. extension_function_adapter on `AnalyticsHelper.logOnboardingStateChanged` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/AnalyticsExtensions.kt:79:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'AnalyticsHelper.logOnboardingStateChanged' retroactively augments type without subclassing

### 25. extension_function_adapter on `ConnectivityManager.isCurrentlyConnected` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/util/ConnectivityManagerNetworkMonitor.kt:91:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'ConnectivityManager.isCurrentlyConnected' retroactively augments type without subclassing

### 26. extension_function_adapter on `RecentSearchQueryEntity.asExternalModel` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/model/RecentSearchQuery.kt:28:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'RecentSearchQueryEntity.asExternalModel' retroactively augments type without subclassing

### 27. extension_function_adapter on `NetworkTopic.asEntity` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/model/Topic.kt:22:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'NetworkTopic.asEntity' retroactively augments type without subclassing

### 28. extension_function_adapter on `NetworkNewsResource.asEntity` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/model/NewsResource.kt:27:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'NetworkNewsResource.asEntity' retroactively augments type without subclassing

### 29. extension_function_adapter on `NetworkNewsResource.topicEntityShells` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/model/NewsResource.kt:41:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'NetworkNewsResource.topicEntityShells' retroactively augments type without subclassing

### 30. extension_function_adapter on `NetworkNewsResource.topicCrossReferences` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/model/NewsResource.kt:53:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'NetworkNewsResource.topicCrossReferences' retroactively augments type without subclassing

### 31. extension_function_adapter on `NetworkNewsResource.asExternalModel` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/model/NewsResource.kt:61:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'NetworkNewsResource.asExternalModel' retroactively augments type without subclassing

### 32. extension_function_adapter on `Flow<SearchResult>.mapToUserSearchResult` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/domain/src/main/kotlin/com/google/samples/apps/nowinandroid/core/domain/GetSearchContentsUseCase.kt:45:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Flow<SearchResult>.mapToUserSearchResult' retroactively augments type without subclassing

### 33. extension_function_adapter on `Context.ensureNotificationChannelExists` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/notifications/src/main/kotlin/com/google/samples/apps/nowinandroid/core/notifications/SystemTrayNotifier.kt:137:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Context.ensureNotificationChannelExists' retroactively augments type without subclassing

### 34. extension_function_adapter on `NewsResource.newsDeepLinkUri` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/notifications/src/main/kotlin/com/google/samples/apps/nowinandroid/core/notifications/SystemTrayNotifier.kt:167:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'NewsResource.newsDeepLinkUri' retroactively augments type without subclassing

### 35. extension_function_adapter on `DpRect.toInsets` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/SnackbarInsetsScreenshotTests.kt:327:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'DpRect.toInsets' retroactively augments type without subclassing

### 36. extension_function_adapter on `DpRect.toInsets` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/SnackbarInsetsScreenshotTests.kt:329:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'DpRect.toInsets' retroactively augments type without subclassing

### 37. extension_function_adapter on `Modifier.notificationDot` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/ui/NiaApp.kt:281:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Modifier.notificationDot' retroactively augments type without subclassing

### 38. extension_function_adapter on `ComponentActivity.isSystemInDarkTheme` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/util/UiExtensions.kt:37:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'ComponentActivity.isSystemInDarkTheme' retroactively augments type without subclassing

### 39. extension_function_adapter on `BuildFeatures.isIsolatedProjectsEnabled` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/RootPlugin.kt:36:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'BuildFeatures.isIsolatedProjectsEnabled' retroactively augments type without subclassing

### 40. extension_function_adapter on `Lint.configure` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/AndroidLintConventionPlugin.kt:44:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Lint.configure' retroactively augments type without subclassing

### 41. extension_function_adapter on `Project.configurePrintApksTask` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/PrintTestApks.kt:40:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Project.configurePrintApksTask' retroactively augments type without subclassing

### 42. extension_function_adapter on `Provider<String>.onlyIfTrue` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/AndroidCompose.kt:47:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Provider<String>.onlyIfTrue' retroactively augments type without subclassing

### 43. extension_function_adapter on `String.capitalized` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/Badging.kt:107:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'String.capitalized' retroactively augments type without subclassing

### 44. extension_function_adapter on `Project.configureKotlinJvm` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/KotlinAndroid.kt:63:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Project.configureKotlinJvm' retroactively augments type without subclassing

### 45. extension_function_adapter on `Project.configureKotlin` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/KotlinAndroid.kt:77:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Project.configureKotlin' retroactively augments type without subclassing

### 46. extension_function_adapter on `Project.configureSpotlessForAndroid` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/Spotless.kt:24:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Project.configureSpotlessForAndroid' retroactively augments type without subclassing

### 47. extension_function_adapter on `Project.configureSpotlessForJvm` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/Spotless.kt:36:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Project.configureSpotlessForJvm' retroactively augments type without subclassing

### 48. extension_function_adapter on `Project.configureSpotlessForRootProject` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/Spotless.kt:40:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Project.configureSpotlessForRootProject' retroactively augments type without subclassing

### 49. extension_function_adapter on `Project.configureSpotlessCommon` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/Spotless.kt:62:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Project.configureSpotlessCommon' retroactively augments type without subclassing

### 50. extension_function_adapter on `String.capitalize` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/Jacoco.kt:49:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'String.capitalize' retroactively augments type without subclassing

### 51. extension_function_adapter on `Project.configureGraphTasks` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/Graph.kt:128:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Project.configureGraphTasks' retroactively augments type without subclassing

### 52. extension_function_adapter on `String.alias` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/Graph.kt:269:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'String.alias' retroactively augments type without subclassing

### 53. extension_function_adapter on `Dependency.link` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/Graph.kt:276:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Dependency.link' retroactively augments type without subclassing

### 54. extension_function_adapter on `PluginType.classDef` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/Graph.kt:289:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'PluginType.classDef' retroactively augments type without subclassing

### 55. extension_function_adapter on `String.trimTrailingNewLines` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/Graph.kt:350:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'String.trimTrailingNewLines' retroactively augments type without subclassing

### 56. extension_function_adapter on `UiDevice.flingElementDownUp` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/Utils.kt:35:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'UiDevice.flingElementDownUp' retroactively augments type without subclassing

### 57. extension_function_adapter on `UiDevice.waitAndFindObject` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/Utils.kt:48:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'UiDevice.waitAndFindObject' retroactively augments type without subclassing

### 58. extension_function_adapter on `UiDevice.dumpWindowHierarchy` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/Utils.kt:59:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'UiDevice.dumpWindowHierarchy' retroactively augments type without subclassing

### 59. extension_function_adapter on `MacrobenchmarkScope.allowNotifications` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/GeneralActions.kt:43:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'MacrobenchmarkScope.allowNotifications' retroactively augments type without subclassing

### 60. extension_function_adapter on `MacrobenchmarkScope.startActivityAndAllowNotifications` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/GeneralActions.kt:54:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'MacrobenchmarkScope.startActivityAndAllowNotifications' retroactively augments type without subclassing

### 61. extension_function_adapter on `MacrobenchmarkScope.getTopAppBar` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/GeneralActions.kt:62:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'MacrobenchmarkScope.getTopAppBar' retroactively augments type without subclassing

### 62. extension_function_adapter on `MacrobenchmarkScope.waitForObjectOnTopAppBar` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/GeneralActions.kt:70:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'MacrobenchmarkScope.waitForObjectOnTopAppBar' retroactively augments type without subclassing

### 63. extension_function_adapter on `MacrobenchmarkScope.forYouWaitForContent` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/foryou/ForYouActions.kt:28:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'MacrobenchmarkScope.forYouWaitForContent' retroactively augments type without subclassing

### 64. extension_function_adapter on `MacrobenchmarkScope.forYouSelectTopics` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/foryou/ForYouActions.kt:42:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'MacrobenchmarkScope.forYouSelectTopics' retroactively augments type without subclassing

### 65. extension_function_adapter on `MacrobenchmarkScope.forYouScrollFeedDownUp` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/foryou/ForYouActions.kt:93:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'MacrobenchmarkScope.forYouScrollFeedDownUp' retroactively augments type without subclassing

### 66. extension_function_adapter on `MacrobenchmarkScope.setAppTheme` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/foryou/ForYouActions.kt:98:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'MacrobenchmarkScope.setAppTheme' retroactively augments type without subclassing

### 67. extension_function_adapter on `MacrobenchmarkScope.goToBookmarksScreen` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/bookmarks/BookmarksActions.kt:23:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'MacrobenchmarkScope.goToBookmarksScreen' retroactively augments type without subclassing

### 68. extension_function_adapter on `MacrobenchmarkScope.goToInterestsScreen` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/interests/InterestsActions.kt:25:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'MacrobenchmarkScope.goToInterestsScreen' retroactively augments type without subclassing

### 69. extension_function_adapter on `MacrobenchmarkScope.interestsScrollTopicsDownUp` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/interests/InterestsActions.kt:35:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'MacrobenchmarkScope.interestsScrollTopicsDownUp' retroactively augments type without subclassing

### 70. extension_function_adapter on `MacrobenchmarkScope.interestsWaitForTopics` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/interests/InterestsActions.kt:41:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'MacrobenchmarkScope.interestsWaitForTopics' retroactively augments type without subclassing

### 71. extension_function_adapter on `MacrobenchmarkScope.interestsToggleBookmarked` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/benchmarks/src/main/kotlin/com/google/samples/apps/nowinandroid/interests/InterestsActions.kt:45:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'MacrobenchmarkScope.interestsToggleBookmarked' retroactively augments type without subclassing

### 72. extension_function_adapter on `AnalyticsHelper.logNewsDeepLinkOpen` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/ForYouViewModel.kt:150:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'AnalyticsHelper.logNewsDeepLinkOpen' retroactively augments type without subclassing

### 73. extension_function_adapter on `EntryProviderScope<NavKey>.forYouEntry` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/navigation/ForYouEntryProvider.kt:26:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'EntryProviderScope<NavKey>.forYouEntry' retroactively augments type without subclassing

### 74. extension_function_adapter on `EntryProviderScope<NavKey>.topicEntry` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/impl/navigation/TopicEntryProvider.kt:32:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'EntryProviderScope<NavKey>.topicEntry' retroactively augments type without subclassing

### 75. extension_function_adapter on `AnalyticsHelper.logEventSearchTriggered` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchViewModel.kt:137:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'AnalyticsHelper.logEventSearchTriggered' retroactively augments type without subclassing

### 76. extension_function_adapter on `EntryProviderScope<NavKey>.searchEntry` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/navigation/SearchEntryProvider.kt:27:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'EntryProviderScope<NavKey>.searchEntry' retroactively augments type without subclassing

### 77. extension_function_adapter on `EntryProviderScope<NavKey>.bookmarksEntry` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/bookmarks/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/bookmarks/impl/navigation/BookmarksEntryProvider.kt:30:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'EntryProviderScope<NavKey>.bookmarksEntry' retroactively augments type without subclassing

### 78. extension_function_adapter on `EntryProviderScope<NavKey>.interestsEntry` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/impl/navigation/InterestsEntryProvider.kt:32:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'EntryProviderScope<NavKey>.interestsEntry' retroactively augments type without subclassing

### 79. extension_function_adapter on `List<WorkInfo>.anyRunning` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/status/WorkManagerSyncManager.kt:55:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'List<WorkInfo>.anyRunning' retroactively augments type without subclassing

### 80. extension_function_adapter on `AnalyticsHelper.logSyncStarted` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/workers/AnalyticsExtensions.kt:22:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'AnalyticsHelper.logSyncStarted' retroactively augments type without subclassing

### 81. extension_function_adapter on `AnalyticsHelper.logSyncFinished` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/workers/AnalyticsExtensions.kt:27:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'AnalyticsHelper.logSyncFinished' retroactively augments type without subclassing

### 82. extension_function_adapter on `Context.syncForegroundInfo` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/initializers/SyncWorkHelpers.kt:44:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Context.syncForegroundInfo' retroactively augments type without subclassing

### 83. extension_function_adapter on `Context.syncWorkNotification` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `extension_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/initializers/SyncWorkHelpers.kt:53:1`
- **Summary:** Retroactive extension augmenting types with domain methods without subclassing.
- **Evidence Trail:**
  - `+90%` (KOTLIN_EXTENSION_FUNCTION): Extension function 'Context.syncWorkNotification' retroactively augments type without subclassing

### 84. delegated_property_lazy on `isLoading` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/NewsResourceCard.kt:182:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'isLoading' delegates accessor behavior via 'remember { mutableStateOf(true) }'

### 85. delegated_property_lazy on `isError` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/NewsResourceCard.kt:183:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'isError' delegates accessor behavior via 'remember { mutableStateOf(false) }'

### 86. delegated_property_lazy on `rotationAnim` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/LoadingWheel.kt:79:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'rotationAnim' delegates accessor behavior via 'infiniteTransition.animateFloat('

### 87. delegated_property_lazy on `isLoading` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/DynamicAsyncImage.kt:56:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'isLoading' delegates accessor behavior via 'remember { mutableStateOf(true) }'

### 88. delegated_property_lazy on `isError` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/DynamicAsyncImage.kt:57:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'isError' delegates accessor behavior via 'remember { mutableStateOf(false) }'

### 89. delegated_property_lazy on `currentTopColor` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Background.kt:82:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'currentTopColor' delegates accessor behavior via 'rememberUpdatedState(gradientColors.top)'

### 90. delegated_property_lazy on `currentBottomColor` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Background.kt:83:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'currentBottomColor' delegates accessor behavior via 'rememberUpdatedState(gradientColors.bottom)'

### 91. delegated_property_lazy on `pressedOffset` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/Scrollbar.kt:208:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'pressedOffset' delegates accessor behavior via 'remember { mutableStateOf(Offset.Unspecified) }'

### 92. delegated_property_lazy on `draggedOffset` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/Scrollbar.kt:209:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'draggedOffset' delegates accessor behavior via 'remember { mutableStateOf(Offset.Unspecified) }'

### 93. delegated_property_lazy on `interactionThumbTravelPercent` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/Scrollbar.kt:213:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'interactionThumbTravelPercent' delegates accessor behavior via 'remember { mutableFloatStateOf(Float.NaN) }'

### 94. delegated_property_lazy on `track` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/Scrollbar.kt:215:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'track' delegates accessor behavior via 'remember { mutableStateOf(ScrollbarTrack(packedValue = 0)) }'

### 95. delegated_property_lazy on `packedValue` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/Scrollbar.kt:77:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'packedValue' delegates accessor behavior via 'mutableLongStateOf(0L)'

### 96. delegated_property_lazy on `state` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/AppScrollbars.kt:221:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'state' delegates accessor behavior via 'remember { mutableStateOf(Dormant) }'

### 97. delegated_property_lazy on `pressed` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/AppScrollbars.kt:222:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'pressed' delegates accessor behavior via 'interactionSource.collectIsPressedAsState()'

### 98. delegated_property_lazy on `hovered` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/AppScrollbars.kt:223:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'hovered' delegates accessor behavior via 'interactionSource.collectIsHoveredAsState()'

### 99. delegated_property_lazy on `dragged` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/AppScrollbars.kt:224:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'dragged' delegates accessor behavior via 'interactionSource.collectIsDraggedAsState()'

### 100. delegated_property_lazy on `percentage` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/ThumbExt.kt:78:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'percentage' delegates accessor behavior via 'remember { mutableFloatStateOf(Float.NaN) }'

### 101. delegated_property_lazy on `itemCount` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/ThumbExt.kt:79:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'itemCount' delegates accessor behavior via 'rememberUpdatedState(itemsAvailable)'

### 102. delegated_property_lazy on `darkMode` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/screenshot-testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/util/ScreenshotHelper.kt:168:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'darkMode' delegates accessor behavior via 'mutableStateOf(true)'

### 103. delegated_property_lazy on `dynamicTheming` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/screenshot-testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/util/ScreenshotHelper.kt:169:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'dynamicTheming' delegates accessor behavior via 'mutableStateOf(false)'

### 104. delegated_property_lazy on `androidTheme` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/screenshot-testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/util/ScreenshotHelper.kt:170:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'androidTheme' delegates accessor behavior via 'mutableStateOf(false)'

### 105. delegated_property_lazy on `currentTopLevelKey` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/navigation/src/main/kotlin/com/google/samples/apps/nowinandroid/core/navigation/NavigationState.kt:66:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'currentTopLevelKey' delegates accessor behavior via 'derivedStateOf { topLevelStack.last() }'

### 106. delegated_property_lazy on `currentKey` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/navigation/src/main/kotlin/com/google/samples/apps/nowinandroid/core/navigation/NavigationState.kt:77:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'currentKey' delegates accessor behavior via 'derivedStateOf { currentSubStack.last() }'

### 107. delegated_property_lazy on `navigateUp` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/ui/NavigationTest.kt:89:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'navigateUp' delegates accessor behavior via 'composeTestRule.stringResource(FeatureForyouR.string.feature_foryou_api_navigate_up)'

### 108. delegated_property_lazy on `forYou` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/ui/NavigationTest.kt:90:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'forYou' delegates accessor behavior via 'composeTestRule.stringResource(FeatureForyouR.string.feature_foryou_api_title)'

### 109. delegated_property_lazy on `interests` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/ui/NavigationTest.kt:91:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'interests' delegates accessor behavior via 'composeTestRule.stringResource(FeatureSearchR.string.feature_search_api_interests)'

### 110. delegated_property_lazy on `appName` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/ui/NavigationTest.kt:93:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'appName' delegates accessor behavior via 'composeTestRule.stringResource(R.string.app_name)'

### 111. delegated_property_lazy on `saved` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/ui/NavigationTest.kt:94:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'saved' delegates accessor behavior via 'composeTestRule.stringResource(BookmarksR.string.feature_bookmarks_api_title)'

### 112. delegated_property_lazy on `settings` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/ui/NavigationTest.kt:95:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'settings' delegates accessor behavior via 'composeTestRule.stringResource(SettingsR.string.feature_settings_impl_top_app_bar_action_icon_description)'

### 113. delegated_property_lazy on `brand` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/ui/NavigationTest.kt:96:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'brand' delegates accessor behavior via 'composeTestRule.stringResource(SettingsR.string.feature_settings_impl_brand_android)'

### 114. delegated_property_lazy on `ok` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/ui/NavigationTest.kt:97:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'ok' delegates accessor behavior via 'composeTestRule.stringResource(SettingsR.string.feature_settings_impl_dismiss_dialog_button_text)'

### 115. delegated_property_lazy on `currentContentUnderTest` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/DeviceConfigurationOverrideWindowInsets.kt:36:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'currentContentUnderTest' delegates accessor behavior via 'rememberUpdatedState(contentUnderTest)'

### 116. delegated_property_lazy on `currentWindowInsets` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/DeviceConfigurationOverrideWindowInsets.kt:37:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'currentWindowInsets' delegates accessor behavior via 'rememberUpdatedState(windowInsets)'

### 117. delegated_property_lazy on `viewModel` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/MainActivity.kt:76:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'viewModel' delegates accessor behavior via 'viewModels()'

### 118. delegated_property_lazy on `themeSettings` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/MainActivity.kt:84:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'themeSettings' delegates accessor behavior via 'mutableStateOf('

### 119. delegated_property_lazy on `currentTimeZone` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/MainActivity.kt:142:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'currentTimeZone' delegates accessor behavior via 'appState.currentTimeZone.collectAsStateWithLifecycle()'

### 120. delegated_property_lazy on `showSettingsDialog` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/ui/NiaApp.kt:96:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'showSettingsDialog' delegates accessor behavior via 'rememberSaveable { mutableStateOf(false) }'

### 121. delegated_property_lazy on `isOffline` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/ui/NiaApp.kt:108:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'isOffline' delegates accessor behavior via 'appState.isOffline.collectAsStateWithLifecycle()'

### 122. delegated_property_lazy on `unreadNavKeys` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/ui/NiaApp.kt:149:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'unreadNavKeys' delegates accessor behavior via 'appState.topLevelNavKeysWithUnreadResources'

### 123. delegated_property_lazy on `firstChecked` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app-nia-catalog/src/main/kotlin/com/google/samples/apps/niacatalog/ui/Catalog.kt:174:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'firstChecked' delegates accessor behavior via 'rememberSaveable { mutableStateOf(false) }'

### 124. delegated_property_lazy on `secondChecked` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app-nia-catalog/src/main/kotlin/com/google/samples/apps/niacatalog/ui/Catalog.kt:180:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'secondChecked' delegates accessor behavior via 'rememberSaveable { mutableStateOf(true) }'

### 125. delegated_property_lazy on `firstChecked` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app-nia-catalog/src/main/kotlin/com/google/samples/apps/niacatalog/ui/Catalog.kt:203:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'firstChecked' delegates accessor behavior via 'rememberSaveable { mutableStateOf(false) }'

### 126. delegated_property_lazy on `secondChecked` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app-nia-catalog/src/main/kotlin/com/google/samples/apps/niacatalog/ui/Catalog.kt:220:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'secondChecked' delegates accessor behavior via 'rememberSaveable { mutableStateOf(true) }'

### 127. delegated_property_lazy on `firstExpanded` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app-nia-catalog/src/main/kotlin/com/google/samples/apps/niacatalog/ui/Catalog.kt:276:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'firstExpanded' delegates accessor behavior via 'rememberSaveable { mutableStateOf(false) }'

### 128. delegated_property_lazy on `secondExpanded` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app-nia-catalog/src/main/kotlin/com/google/samples/apps/niacatalog/ui/Catalog.kt:283:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'secondExpanded' delegates accessor behavior via 'rememberSaveable { mutableStateOf(true) }'

### 129. delegated_property_lazy on `selectedTabIndex` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app-nia-catalog/src/main/kotlin/com/google/samples/apps/niacatalog/ui/Catalog.kt:322:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'selectedTabIndex' delegates accessor behavior via 'rememberSaveable { mutableIntStateOf(0) }'

### 130. delegated_property_lazy on `selectedItem` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app-nia-catalog/src/main/kotlin/com/google/samples/apps/niacatalog/ui/Catalog.kt:336:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'selectedItem' delegates accessor behavior via 'rememberSaveable { mutableIntStateOf(0) }'

### 131. delegated_property_lazy on `settingsUiState` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/settings/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/settings/impl/SettingsDialog.kt:78:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'settingsUiState' delegates accessor behavior via 'viewModel.settingsUiState.collectAsStateWithLifecycle()'

### 132. delegated_property_lazy on `doneButtonMatcher` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/ForYouScreenTest.kt:47:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'doneButtonMatcher' delegates accessor behavior via 'lazy {'

### 133. delegated_property_lazy on `onboardingUiState` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/ForYouScreen.kt:114:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'onboardingUiState' delegates accessor behavior via 'viewModel.onboardingUiState.collectAsStateWithLifecycle()'

### 134. delegated_property_lazy on `feedState` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/ForYouScreen.kt:115:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'feedState' delegates accessor behavior via 'viewModel.feedState.collectAsStateWithLifecycle()'

### 135. delegated_property_lazy on `isSyncing` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/ForYouScreen.kt:116:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'isSyncing' delegates accessor behavior via 'viewModel.isSyncing.collectAsStateWithLifecycle()'

### 136. delegated_property_lazy on `deepLinkedUserNewsResource` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/ForYouScreen.kt:117:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'deepLinkedUserNewsResource' delegates accessor behavior via 'viewModel.deepLinkedNewsResource.collectAsStateWithLifecycle()'

### 137. delegated_property_lazy on `topicUiState` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/impl/TopicScreen.kt:82:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'topicUiState' delegates accessor behavior via 'viewModel.topicUiState.collectAsStateWithLifecycle()'

### 138. delegated_property_lazy on `newsUiState` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/impl/TopicScreen.kt:83:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'newsUiState' delegates accessor behavior via 'viewModel.newsUiState.collectAsStateWithLifecycle()'

### 139. delegated_property_lazy on `recentSearchQueriesUiState` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchScreen.kt:106:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'recentSearchQueriesUiState' delegates accessor behavior via 'searchViewModel.recentSearchQueriesUiState.collectAsStateWithLifecycle()'

### 140. delegated_property_lazy on `searchResultUiState` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchScreen.kt:107:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'searchResultUiState' delegates accessor behavior via 'searchViewModel.searchResultUiState.collectAsStateWithLifecycle()'

### 141. delegated_property_lazy on `searchQuery` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchScreen.kt:108:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'searchQuery' delegates accessor behavior via 'searchViewModel.searchQuery.collectAsStateWithLifecycle()'

### 142. delegated_property_lazy on `shouldDisplayUndoBookmark` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/bookmarks/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/bookmarks/impl/BookmarksViewModel.kt:44:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'shouldDisplayUndoBookmark' delegates accessor behavior via 'mutableStateOf(false)'

### 143. delegated_property_lazy on `feedState` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/bookmarks/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/bookmarks/impl/BookmarksScreen.kt:86:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'feedState' delegates accessor behavior via 'viewModel.feedUiState.collectAsStateWithLifecycle()'

### 144. delegated_property_lazy on `placeholderText` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/test/kotlin/com/google/samples/apps/nowinandroid/interests/impl/InterestsListDetailScreenTest.kt:85:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'placeholderText' delegates accessor behavior via 'composeTestRule.stringResource(R.string.feature_interests_api_select_an_interest)'

### 145. delegated_property_lazy on `uiState` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `property`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/impl/InterestsScreen.kt:44:1`
- **Summary:** Property behavior delegation using `by lazy`, `by Delegates.observable`, or `ReadOnlyProperty`.
- **Evidence Trail:**
  - `+90%` (KOTLIN_DELEGATED_PROPERTY): Property 'uiState' delegates accessor behavior via 'viewModel.uiState.collectAsStateWithLifecycle()'

### 146. sealed_hierarchy_adt on `NewsFeedUiState` (95% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/NewsFeed.kt:108:1`
- **Summary:** Exhaustive sum types / Algebraic Data Types representing closed polymorphic domain models.
- **Evidence Trail:**
  - `+95%` (KOTLIN_SEALED_HIERARCHY): Sealed type 'NewsFeedUiState' (sealed_interface) defines an Algebraic Data Type (ADT) hierarchy for exhaustive pattern matching

### 147. sealed_hierarchy_adt on `Result` (95% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/common/src/main/kotlin/com/google/samples/apps/nowinandroid/core/common/result/Result.kt:24:1`
- **Summary:** Exhaustive sum types / Algebraic Data Types representing closed polymorphic domain models.
- **Evidence Trail:**
  - `+95%` (KOTLIN_SEALED_HIERARCHY): Sealed type 'Result' (sealed_interface) defines an Algebraic Data Type (ADT) hierarchy for exhaustive pattern matching

### 148. sealed_hierarchy_adt on `MainActivityUiState` (95% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/MainActivityViewModel.kt:47:1`
- **Summary:** Exhaustive sum types / Algebraic Data Types representing closed polymorphic domain models.
- **Evidence Trail:**
  - `+95%` (KOTLIN_SEALED_HIERARCHY): Sealed type 'MainActivityUiState' (sealed_interface) defines an Algebraic Data Type (ADT) hierarchy for exhaustive pattern matching

### 149. sealed_hierarchy_adt on `SettingsUiState` (95% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/settings/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/settings/impl/SettingsViewModel.kt:84:1`
- **Summary:** Exhaustive sum types / Algebraic Data Types representing closed polymorphic domain models.
- **Evidence Trail:**
  - `+95%` (KOTLIN_SEALED_HIERARCHY): Sealed type 'SettingsUiState' (sealed_interface) defines an Algebraic Data Type (ADT) hierarchy for exhaustive pattern matching

### 150. sealed_hierarchy_adt on `OnboardingUiState` (95% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/OnboardingUiState.kt:24:1`
- **Summary:** Exhaustive sum types / Algebraic Data Types representing closed polymorphic domain models.
- **Evidence Trail:**
  - `+95%` (KOTLIN_SEALED_HIERARCHY): Sealed type 'OnboardingUiState' (sealed_interface) defines an Algebraic Data Type (ADT) hierarchy for exhaustive pattern matching

### 151. sealed_hierarchy_adt on `TopicUiState` (95% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/impl/TopicViewModel.kt:161:1`
- **Summary:** Exhaustive sum types / Algebraic Data Types representing closed polymorphic domain models.
- **Evidence Trail:**
  - `+95%` (KOTLIN_SEALED_HIERARCHY): Sealed type 'TopicUiState' (sealed_interface) defines an Algebraic Data Type (ADT) hierarchy for exhaustive pattern matching

### 152. sealed_hierarchy_adt on `NewsUiState` (95% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/impl/TopicViewModel.kt:167:1`
- **Summary:** Exhaustive sum types / Algebraic Data Types representing closed polymorphic domain models.
- **Evidence Trail:**
  - `+95%` (KOTLIN_SEALED_HIERARCHY): Sealed type 'NewsUiState' (sealed_interface) defines an Algebraic Data Type (ADT) hierarchy for exhaustive pattern matching

### 153. sealed_hierarchy_adt on `SearchResultUiState` (95% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchResultUiState.kt:22:1`
- **Summary:** Exhaustive sum types / Algebraic Data Types representing closed polymorphic domain models.
- **Evidence Trail:**
  - `+95%` (KOTLIN_SEALED_HIERARCHY): Sealed type 'SearchResultUiState' (sealed_interface) defines an Algebraic Data Type (ADT) hierarchy for exhaustive pattern matching

### 154. sealed_hierarchy_adt on `RecentSearchQueriesUiState` (95% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/RecentSearchQueriesUiState.kt:21:1`
- **Summary:** Exhaustive sum types / Algebraic Data Types representing closed polymorphic domain models.
- **Evidence Trail:**
  - `+95%` (KOTLIN_SEALED_HIERARCHY): Sealed type 'RecentSearchQueriesUiState' (sealed_interface) defines an Algebraic Data Type (ADT) hierarchy for exhaustive pattern matching

### 155. sealed_hierarchy_adt on `InterestsUiState` (95% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/impl/InterestsViewModel.kt:84:1`
- **Summary:** Exhaustive sum types / Algebraic Data Types representing closed polymorphic domain models.
- **Evidence Trail:**
  - `+95%` (KOTLIN_SEALED_HIERARCHY): Sealed type 'InterestsUiState' (sealed_interface) defines an Algebraic Data Type (ADT) hierarchy for exhaustive pattern matching

### 156. inline_value_class on `ScrollbarStateValue` (95% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `value_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/Scrollbar.kt:126:1`
- **Summary:** Zero-runtime-overhead strongly typed domain primitives preventing primitive obsession.
- **Evidence Trail:**
  - `+95%` (KOTLIN_INLINE_VALUE_CLASS): Value class 'ScrollbarStateValue' encapsulates strongly typed domain primitive with zero runtime allocation overhead

### 157. inline_value_class on `ScrollbarTrack` (95% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `value_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/Scrollbar.kt:135:1`
- **Summary:** Zero-runtime-overhead strongly typed domain primitives preventing primitive obsession.
- **Evidence Trail:**
  - `+95%` (KOTLIN_INLINE_VALUE_CLASS): Value class 'ScrollbarTrack' encapsulates strongly typed domain primitive with zero runtime allocation overhead

### 158. operator_overloading_dsl on `invoke` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `operator_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/domain/src/main/kotlin/com/google/samples/apps/nowinandroid/core/domain/GetRecentSearchQueriesUseCase.kt:30:1`
- **Summary:** Custom `operator fun` implementations enabling expressive mathematical and collection DSLs.
- **Evidence Trail:**
  - `+90%` (KOTLIN_OPERATOR_OVERLOADING): Operator function 'invoke' overloads language operators for domain expression semantics

### 159. operator_overloading_dsl on `invoke` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `operator_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/domain/src/main/kotlin/com/google/samples/apps/nowinandroid/core/domain/GetFollowableTopicsUseCase.kt:40:1`
- **Summary:** Custom `operator fun` implementations enabling expressive mathematical and collection DSLs.
- **Evidence Trail:**
  - `+90%` (KOTLIN_OPERATOR_OVERLOADING): Operator function 'invoke' overloads language operators for domain expression semantics

### 160. operator_overloading_dsl on `invoke` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `operator_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/util/ProfileVerifierLogger.kt:58:1`
- **Summary:** Custom `operator fun` implementations enabling expressive mathematical and collection DSLs.
- **Evidence Trail:**
  - `+90%` (KOTLIN_OPERATOR_OVERLOADING): Operator function 'invoke' overloads language operators for domain expression semantics

### 161. operator_overloading_dsl on `invoke` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `operator_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/Graph.kt:65:1`
- **Summary:** Custom `operator fun` implementations enabling expressive mathematical and collection DSLs.
- **Evidence Trail:**
  - `+90%` (KOTLIN_OPERATOR_OVERLOADING): Operator function 'invoke' overloads language operators for domain expression semantics

### 162. operator_overloading_dsl on `invoke` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `operator_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/Graph.kt:167:1`
- **Summary:** Custom `operator fun` implementations enabling expressive mathematical and collection DSLs.
- **Evidence Trail:**
  - `+90%` (KOTLIN_OPERATOR_OVERLOADING): Operator function 'invoke' overloads language operators for domain expression semantics

### 163. operator_overloading_dsl on `invoke` (90% [VERY_HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `operator_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/Graph.kt:312:1`
- **Summary:** Custom `operator fun` implementations enabling expressive mathematical and collection DSLs.
- **Evidence Trail:**
  - `+90%` (KOTLIN_OPERATOR_OVERLOADING): Operator function 'invoke' overloads language operators for domain expression semantics

### 164. scope_function_chain on `getNewsResources` (80% [HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestNewsRepository.kt:37:1`
- **Summary:** Idiomatic Kotlin scope functions structuring object initialization and transformation pipelines.
- **Evidence Trail:**
  - `+80%` (KOTLIN_SCOPE_FUNCTION_PIPELINE): Function 'getNewsResources' coordinates object lifecycle via 2 scope functions (let, let)

### 165. scope_function_chain on `navigatingToTopicFromForYou_showsTopicDetails` (80% [HIGH])
- **Category:** `kotlin_idiomatic`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/ui/NavigationTest.kt:287:1`
- **Summary:** Idiomatic Kotlin scope functions structuring object initialization and transformation pipelines.
- **Evidence Trail:**
  - `+80%` (KOTLIN_SCOPE_FUNCTION_PIPELINE): Function 'navigatingToTopicFromForYou_showsTopicDetails' coordinates object lifecycle via 2 scope functions (apply, apply)

### 166. structured_concurrency_scope on `NiaAppStateTest` (90% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/NiaAppStateTest.kt:52:1`
- **Summary:** Parent-child lifecycle-bound coroutine scopes preventing unconfined background leaks.
- **Evidence Trail:**
  - `+90%` (COROUTINES_STRUCTURED_SCOPE): Type 'NiaAppStateTest' bounds asynchronous jobs within structured CoroutineScope

### 167. structured_concurrency_scope on `SnackbarScreenshotTests` (90% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/SnackbarScreenshotTests.kt:73:1`
- **Summary:** Parent-child lifecycle-bound coroutine scopes preventing unconfined background leaks.
- **Evidence Trail:**
  - `+90%` (COROUTINES_STRUCTURED_SCOPE): Type 'SnackbarScreenshotTests' bounds asynchronous jobs within structured CoroutineScope

### 168. structured_concurrency_scope on `SnackbarInsetsScreenshotTests` (90% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/SnackbarInsetsScreenshotTests.kt:100:1`
- **Summary:** Parent-child lifecycle-bound coroutine scopes preventing unconfined background leaks.
- **Evidence Trail:**
  - `+90%` (COROUTINES_STRUCTURED_SCOPE): Type 'SnackbarInsetsScreenshotTests' bounds asynchronous jobs within structured CoroutineScope

### 169. structured_concurrency_scope on `MainActivity` (90% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/MainActivity.kt:56:1`
- **Summary:** Parent-child lifecycle-bound coroutine scopes preventing unconfined background leaks.
- **Evidence Trail:**
  - `+90%` (COROUTINES_STRUCTURED_SCOPE): Type 'MainActivity' bounds asynchronous jobs within structured CoroutineScope

### 170. structured_concurrency_scope on `ProfileVerifierLogger` (90% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/util/ProfileVerifierLogger.kt:51:1`
- **Summary:** Parent-child lifecycle-bound coroutine scopes preventing unconfined background leaks.
- **Evidence Trail:**
  - `+90%` (COROUTINES_STRUCTURED_SCOPE): Type 'ProfileVerifierLogger' bounds asynchronous jobs within structured CoroutineScope

### 171. structured_concurrency_scope on `SettingsViewModel` (90% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/settings/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/settings/impl/SettingsViewModel.kt:36:1`
- **Summary:** Parent-child lifecycle-bound coroutine scopes preventing unconfined background leaks.
- **Evidence Trail:**
  - `+90%` (COROUTINES_STRUCTURED_SCOPE): Type 'SettingsViewModel' bounds asynchronous jobs within structured CoroutineScope

### 172. structured_concurrency_scope on `ForYouViewModel` (90% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/ForYouViewModel.kt:45:1`
- **Summary:** Parent-child lifecycle-bound coroutine scopes preventing unconfined background leaks.
- **Evidence Trail:**
  - `+90%` (COROUTINES_STRUCTURED_SCOPE): Type 'ForYouViewModel' bounds asynchronous jobs within structured CoroutineScope

### 173. structured_concurrency_scope on `TopicViewModel` (90% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/impl/TopicViewModel.kt:43:1`
- **Summary:** Parent-child lifecycle-bound coroutine scopes preventing unconfined background leaks.
- **Evidence Trail:**
  - `+90%` (COROUTINES_STRUCTURED_SCOPE): Type 'TopicViewModel' bounds asynchronous jobs within structured CoroutineScope

### 174. structured_concurrency_scope on `SearchViewModel` (90% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchViewModel.kt:43:1`
- **Summary:** Parent-child lifecycle-bound coroutine scopes preventing unconfined background leaks.
- **Evidence Trail:**
  - `+90%` (COROUTINES_STRUCTURED_SCOPE): Type 'SearchViewModel' bounds asynchronous jobs within structured CoroutineScope

### 175. structured_concurrency_scope on `BookmarksViewModel` (90% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/bookmarks/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/bookmarks/impl/BookmarksViewModel.kt:39:1`
- **Summary:** Parent-child lifecycle-bound coroutine scopes preventing unconfined background leaks.
- **Evidence Trail:**
  - `+90%` (COROUTINES_STRUCTURED_SCOPE): Type 'BookmarksViewModel' bounds asynchronous jobs within structured CoroutineScope

### 176. structured_concurrency_scope on `InterestsViewModel` (90% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/impl/InterestsViewModel.kt:38:1`
- **Summary:** Parent-child lifecycle-bound coroutine scopes preventing unconfined background leaks.
- **Evidence Trail:**
  - `+90%` (COROUTINES_STRUCTURED_SCOPE): Type 'InterestsViewModel' bounds asynchronous jobs within structured CoroutineScope

### 177. stateflow_reactive_stream on `TestUserDataRepository` (95% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestUserDataRepository.kt:38:1`
- **Summary:** Hot reactive state stream emitting updates to subscribed collectors in presentation/domain layers.
- **Evidence Trail:**
  - `+95%` (COROUTINES_STATEFLOW_STREAM): Type 'TestUserDataRepository' defines 1 hot StateFlow/SharedFlow reactive stream(s) (_userData)

### 178. stateflow_reactive_stream on `MainActivityViewModel` (95% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/MainActivityViewModel.kt:35:1`
- **Summary:** Hot reactive state stream emitting updates to subscribed collectors in presentation/domain layers.
- **Evidence Trail:**
  - `+95%` (COROUTINES_STATEFLOW_STREAM): Type 'MainActivityViewModel' defines 1 hot StateFlow/SharedFlow reactive stream(s) (uiState)

### 179. stateflow_reactive_stream on `TopicViewModel` (95% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/impl/TopicViewModel.kt:43:1`
- **Summary:** Hot reactive state stream emitting updates to subscribed collectors in presentation/domain layers.
- **Evidence Trail:**
  - `+95%` (COROUTINES_STATEFLOW_STREAM): Type 'TopicViewModel' defines 2 hot StateFlow/SharedFlow reactive stream(s) (topicUiState, newsUiState)

### 180. stateflow_reactive_stream on `InterestsViewModel` (95% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/impl/InterestsViewModel.kt:38:1`
- **Summary:** Hot reactive state stream emitting updates to subscribed collectors in presentation/domain layers.
- **Evidence Trail:**
  - `+95%` (COROUTINES_STATEFLOW_STREAM): Type 'InterestsViewModel' defines 1 hot StateFlow/SharedFlow reactive stream(s) (uiState)

### 181. suspending_function_async on `insertTopics` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/core/database/dao/TopicDaoTest.kt:106:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'insertTopics' enables non-blocking asynchronous continuation

### 182. suspending_function_async on `insertAll` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/dao/TopicFtsDao.kt:32:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'insertAll' enables non-blocking asynchronous continuation

### 183. suspending_function_async on `insertOrReplaceRecentSearchQuery` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/dao/RecentSearchQueryDao.kt:34:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'insertOrReplaceRecentSearchQuery' enables non-blocking asynchronous continuation

### 184. suspending_function_async on `clearRecentSearchQueries` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/dao/RecentSearchQueryDao.kt:37:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'clearRecentSearchQueries' enables non-blocking asynchronous continuation

### 185. suspending_function_async on `insertAll` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/dao/NewsResourceFtsDao.kt:32:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'insertAll' enables non-blocking asynchronous continuation

### 186. suspending_function_async on `upsertNewsResources` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/dao/NewsResourceDao.kt:103:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'upsertNewsResources' enables non-blocking asynchronous continuation

### 187. suspending_function_async on `deleteNewsResources` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/dao/NewsResourceDao.kt:119:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'deleteNewsResources' enables non-blocking asynchronous continuation

### 188. suspending_function_async on `getOneOffTopicEntities` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/dao/TopicDao.kt:44:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getOneOffTopicEntities' enables non-blocking asynchronous continuation

### 189. suspending_function_async on `insertOrIgnoreTopics` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/dao/TopicDao.kt:58:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'insertOrIgnoreTopics' enables non-blocking asynchronous continuation

### 190. suspending_function_async on `upsertTopics` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/dao/TopicDao.kt:64:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'upsertTopics' enables non-blocking asynchronous continuation

### 191. suspending_function_async on `deleteTopics` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/dao/TopicDao.kt:75:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'deleteTopics' enables non-blocking asynchronous continuation

### 192. suspending_function_async on `setFollowedTopicIds` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/repository/FakeUserDataRepository.kt:40:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setFollowedTopicIds' enables non-blocking asynchronous continuation

### 193. suspending_function_async on `setTopicIdFollowed` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/repository/FakeUserDataRepository.kt:43:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setTopicIdFollowed' enables non-blocking asynchronous continuation

### 194. suspending_function_async on `setNewsResourceBookmarked` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/repository/FakeUserDataRepository.kt:46:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setNewsResourceBookmarked' enables non-blocking asynchronous continuation

### 195. suspending_function_async on `setNewsResourceViewed` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/repository/FakeUserDataRepository.kt:50:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setNewsResourceViewed' enables non-blocking asynchronous continuation

### 196. suspending_function_async on `setThemeBrand` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/repository/FakeUserDataRepository.kt:53:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setThemeBrand' enables non-blocking asynchronous continuation

### 197. suspending_function_async on `setDarkThemeConfig` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/repository/FakeUserDataRepository.kt:57:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setDarkThemeConfig' enables non-blocking asynchronous continuation

### 198. suspending_function_async on `setDynamicColorPreference` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/repository/FakeUserDataRepository.kt:61:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setDynamicColorPreference' enables non-blocking asynchronous continuation

### 199. suspending_function_async on `setShouldHideOnboarding` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/repository/FakeUserDataRepository.kt:65:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setShouldHideOnboarding' enables non-blocking asynchronous continuation

### 200. suspending_function_async on `syncWith` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/repository/FakeTopicsRepository.kt:61:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'syncWith' enables non-blocking asynchronous continuation

### 201. suspending_function_async on `insertOrReplaceRecentSearch` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/repository/FakeRecentSearchRepository.kt:29:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'insertOrReplaceRecentSearch' enables non-blocking asynchronous continuation

### 202. suspending_function_async on `clearRecentSearches` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/repository/FakeRecentSearchRepository.kt:34:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'clearRecentSearches' enables non-blocking asynchronous continuation

### 203. suspending_function_async on `syncWith` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/repository/FakeNewsRepository.kt:70:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'syncWith' enables non-blocking asynchronous continuation

### 204. suspending_function_async on `populateFtsData` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/repository/FakeSearchContentsRepository.kt:30:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'populateFtsData' enables non-blocking asynchronous continuation

### 205. suspending_function_async on `getTopics` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/NiaNetworkDataSource.kt:27:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getTopics' enables non-blocking asynchronous continuation

### 206. suspending_function_async on `getNewsResources` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/NiaNetworkDataSource.kt:29:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getNewsResources' enables non-blocking asynchronous continuation

### 207. suspending_function_async on `getTopicChangeList` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/NiaNetworkDataSource.kt:31:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getTopicChangeList' enables non-blocking asynchronous continuation

### 208. suspending_function_async on `getNewsResourceChangeList` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/NiaNetworkDataSource.kt:33:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getNewsResourceChangeList' enables non-blocking asynchronous continuation

### 209. suspending_function_async on `getTopics` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/demo/DemoNiaNetworkDataSource.kt:45:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getTopics' enables non-blocking asynchronous continuation

### 210. suspending_function_async on `getNewsResources` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/demo/DemoNiaNetworkDataSource.kt:48:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getNewsResources' enables non-blocking asynchronous continuation

### 211. suspending_function_async on `getTopicChangeList` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/demo/DemoNiaNetworkDataSource.kt:51:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getTopicChangeList' enables non-blocking asynchronous continuation

### 212. suspending_function_async on `getNewsResourceChangeList` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/demo/DemoNiaNetworkDataSource.kt:54:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getNewsResourceChangeList' enables non-blocking asynchronous continuation

### 213. suspending_function_async on `getTopics` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/retrofit/RetrofitNiaNetwork.kt:93:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getTopics' enables non-blocking asynchronous continuation

### 214. suspending_function_async on `getNewsResources` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/retrofit/RetrofitNiaNetwork.kt:96:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getNewsResources' enables non-blocking asynchronous continuation

### 215. suspending_function_async on `getTopicChangeList` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/retrofit/RetrofitNiaNetwork.kt:99:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getTopicChangeList' enables non-blocking asynchronous continuation

### 216. suspending_function_async on `getNewsResourceChangeList` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/retrofit/RetrofitNiaNetwork.kt:102:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getNewsResourceChangeList' enables non-blocking asynchronous continuation

### 217. suspending_function_async on `insertOrReplaceRecentSearch` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestRecentSearchRepository.kt:31:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'insertOrReplaceRecentSearch' enables non-blocking asynchronous continuation

### 218. suspending_function_async on `clearRecentSearches` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestRecentSearchRepository.kt:35:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'clearRecentSearches' enables non-blocking asynchronous continuation

### 219. suspending_function_async on `populateFtsData` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestSearchContentsRepository.kt:34:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'populateFtsData' enables non-blocking asynchronous continuation

### 220. suspending_function_async on `syncWith` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestNewsRepository.kt:58:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'syncWith' enables non-blocking asynchronous continuation

### 221. suspending_function_async on `syncWith` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestTopicsRepository.kt:46:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'syncWith' enables non-blocking asynchronous continuation

### 222. suspending_function_async on `setFollowedTopicIds` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestUserDataRepository.kt:48:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setFollowedTopicIds' enables non-blocking asynchronous continuation

### 223. suspending_function_async on `setTopicIdFollowed` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestUserDataRepository.kt:52:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setTopicIdFollowed' enables non-blocking asynchronous continuation

### 224. suspending_function_async on `setNewsResourceBookmarked` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestUserDataRepository.kt:64:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setNewsResourceBookmarked' enables non-blocking asynchronous continuation

### 225. suspending_function_async on `setNewsResourceViewed` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestUserDataRepository.kt:76:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setNewsResourceViewed' enables non-blocking asynchronous continuation

### 226. suspending_function_async on `setThemeBrand` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestUserDataRepository.kt:91:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setThemeBrand' enables non-blocking asynchronous continuation

### 227. suspending_function_async on `setDarkThemeConfig` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestUserDataRepository.kt:97:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setDarkThemeConfig' enables non-blocking asynchronous continuation

### 228. suspending_function_async on `setDynamicColorPreference` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestUserDataRepository.kt:103:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setDynamicColorPreference' enables non-blocking asynchronous continuation

### 229. suspending_function_async on `setShouldHideOnboarding` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestUserDataRepository.kt:109:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setShouldHideOnboarding' enables non-blocking asynchronous continuation

### 230. suspending_function_async on `setFollowedTopicIds` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/NiaPreferencesDataSource.kt:62:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setFollowedTopicIds' enables non-blocking asynchronous continuation

### 231. suspending_function_async on `setTopicIdFollowed` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/NiaPreferencesDataSource.kt:76:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setTopicIdFollowed' enables non-blocking asynchronous continuation

### 232. suspending_function_async on `setThemeBrand` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/NiaPreferencesDataSource.kt:93:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setThemeBrand' enables non-blocking asynchronous continuation

### 233. suspending_function_async on `setDynamicColorPreference` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/NiaPreferencesDataSource.kt:104:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setDynamicColorPreference' enables non-blocking asynchronous continuation

### 234. suspending_function_async on `setDarkThemeConfig` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/NiaPreferencesDataSource.kt:110:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setDarkThemeConfig' enables non-blocking asynchronous continuation

### 235. suspending_function_async on `setNewsResourceBookmarked` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/NiaPreferencesDataSource.kt:123:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setNewsResourceBookmarked' enables non-blocking asynchronous continuation

### 236. suspending_function_async on `setNewsResourceViewed` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/NiaPreferencesDataSource.kt:139:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setNewsResourceViewed' enables non-blocking asynchronous continuation

### 237. suspending_function_async on `setNewsResourcesViewed` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/NiaPreferencesDataSource.kt:143:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setNewsResourcesViewed' enables non-blocking asynchronous continuation

### 238. suspending_function_async on `getChangeListVersions` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/NiaPreferencesDataSource.kt:157:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getChangeListVersions' enables non-blocking asynchronous continuation

### 239. suspending_function_async on `updateChangeListVersion` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/NiaPreferencesDataSource.kt:169:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'updateChangeListVersion' enables non-blocking asynchronous continuation

### 240. suspending_function_async on `setShouldHideOnboarding` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/NiaPreferencesDataSource.kt:189:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setShouldHideOnboarding' enables non-blocking asynchronous continuation

### 241. suspending_function_async on `readFrom` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/UserPreferencesSerializer.kt:32:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'readFrom' enables non-blocking asynchronous continuation

### 242. suspending_function_async on `writeTo` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/UserPreferencesSerializer.kt:40:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'writeTo' enables non-blocking asynchronous continuation

### 243. suspending_function_async on `cleanUp` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/IntToStringIdsMigration.kt:26:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'cleanUp' enables non-blocking asynchronous continuation

### 244. suspending_function_async on `migrate` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/IntToStringIdsMigration.kt:28:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'migrate' enables non-blocking asynchronous continuation

### 245. suspending_function_async on `shouldMigrate` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/IntToStringIdsMigration.kt:48:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'shouldMigrate' enables non-blocking asynchronous continuation

### 246. suspending_function_async on `cleanUp` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/ListToMapMigration.kt:26:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'cleanUp' enables non-blocking asynchronous continuation

### 247. suspending_function_async on `migrate` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/ListToMapMigration.kt:28:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'migrate' enables non-blocking asynchronous continuation

### 248. suspending_function_async on `shouldMigrate` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/ListToMapMigration.kt:55:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'shouldMigrate' enables non-blocking asynchronous continuation

### 249. suspending_function_async on `getChangeListVersions` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/test/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/TestSynchronizer.kt:29:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getChangeListVersions' enables non-blocking asynchronous continuation

### 250. suspending_function_async on `upsertNewsResources` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/test/kotlin/com/google/samples/apps/nowinandroid/core/data/testdoubles/TestNewsResourceDao.kt:95:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'upsertNewsResources' enables non-blocking asynchronous continuation

### 251. suspending_function_async on `deleteNewsResources` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/test/kotlin/com/google/samples/apps/nowinandroid/core/data/testdoubles/TestNewsResourceDao.kt:114:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'deleteNewsResources' enables non-blocking asynchronous continuation

### 252. suspending_function_async on `getTopics` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/test/kotlin/com/google/samples/apps/nowinandroid/core/data/testdoubles/TestNiaNetworkDataSource.kt:54:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getTopics' enables non-blocking asynchronous continuation

### 253. suspending_function_async on `getNewsResources` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/test/kotlin/com/google/samples/apps/nowinandroid/core/data/testdoubles/TestNiaNetworkDataSource.kt:60:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getNewsResources' enables non-blocking asynchronous continuation

### 254. suspending_function_async on `getTopicChangeList` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/test/kotlin/com/google/samples/apps/nowinandroid/core/data/testdoubles/TestNiaNetworkDataSource.kt:66:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getTopicChangeList' enables non-blocking asynchronous continuation

### 255. suspending_function_async on `getNewsResourceChangeList` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/test/kotlin/com/google/samples/apps/nowinandroid/core/data/testdoubles/TestNiaNetworkDataSource.kt:69:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getNewsResourceChangeList' enables non-blocking asynchronous continuation

### 256. suspending_function_async on `getOneOffTopicEntities` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/test/kotlin/com/google/samples/apps/nowinandroid/core/data/testdoubles/TestTopicDao.kt:41:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getOneOffTopicEntities' enables non-blocking asynchronous continuation

### 257. suspending_function_async on `insertOrIgnoreTopics` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/test/kotlin/com/google/samples/apps/nowinandroid/core/data/testdoubles/TestTopicDao.kt:43:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'insertOrIgnoreTopics' enables non-blocking asynchronous continuation

### 258. suspending_function_async on `upsertTopics` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/test/kotlin/com/google/samples/apps/nowinandroid/core/data/testdoubles/TestTopicDao.kt:51:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'upsertTopics' enables non-blocking asynchronous continuation

### 259. suspending_function_async on `deleteTopics` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/test/kotlin/com/google/samples/apps/nowinandroid/core/data/testdoubles/TestTopicDao.kt:56:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'deleteTopics' enables non-blocking asynchronous continuation

### 260. suspending_function_async on `suspendRunCatching` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/SyncUtilities.kt:55:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'suspendRunCatching' enables non-blocking asynchronous continuation

### 261. suspending_function_async on `getChangeListVersions` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/SyncUtilities.kt:29:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getChangeListVersions' enables non-blocking asynchronous continuation

### 262. suspending_function_async on `updateChangeListVersions` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/SyncUtilities.kt:31:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'updateChangeListVersions' enables non-blocking asynchronous continuation

### 263. suspending_function_async on `sync` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/SyncUtilities.kt:36:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'sync' enables non-blocking asynchronous continuation

### 264. suspending_function_async on `syncWith` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/SyncUtilities.kt:48:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'syncWith' enables non-blocking asynchronous continuation

### 265. suspending_function_async on `setFollowedTopicIds` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/UserDataRepository.kt:34:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setFollowedTopicIds' enables non-blocking asynchronous continuation

### 266. suspending_function_async on `setTopicIdFollowed` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/UserDataRepository.kt:39:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setTopicIdFollowed' enables non-blocking asynchronous continuation

### 267. suspending_function_async on `setNewsResourceBookmarked` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/UserDataRepository.kt:44:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setNewsResourceBookmarked' enables non-blocking asynchronous continuation

### 268. suspending_function_async on `setNewsResourceViewed` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/UserDataRepository.kt:49:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setNewsResourceViewed' enables non-blocking asynchronous continuation

### 269. suspending_function_async on `setThemeBrand` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/UserDataRepository.kt:54:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setThemeBrand' enables non-blocking asynchronous continuation

### 270. suspending_function_async on `setDarkThemeConfig` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/UserDataRepository.kt:59:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setDarkThemeConfig' enables non-blocking asynchronous continuation

### 271. suspending_function_async on `setDynamicColorPreference` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/UserDataRepository.kt:64:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setDynamicColorPreference' enables non-blocking asynchronous continuation

### 272. suspending_function_async on `setShouldHideOnboarding` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/UserDataRepository.kt:69:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setShouldHideOnboarding' enables non-blocking asynchronous continuation

### 273. suspending_function_async on `populateFtsData` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/SearchContentsRepository.kt:30:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'populateFtsData' enables non-blocking asynchronous continuation

### 274. suspending_function_async on `insertOrReplaceRecentSearch` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/RecentSearchRepository.kt:35:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'insertOrReplaceRecentSearch' enables non-blocking asynchronous continuation

### 275. suspending_function_async on `clearRecentSearches` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/RecentSearchRepository.kt:40:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'clearRecentSearches' enables non-blocking asynchronous continuation

### 276. suspending_function_async on `syncWith` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/OfflineFirstNewsRepository.kt:66:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'syncWith' enables non-blocking asynchronous continuation

### 277. suspending_function_async on `setFollowedTopicIds` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/OfflineFirstUserDataRepository.kt:37:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setFollowedTopicIds' enables non-blocking asynchronous continuation

### 278. suspending_function_async on `setTopicIdFollowed` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/OfflineFirstUserDataRepository.kt:40:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setTopicIdFollowed' enables non-blocking asynchronous continuation

### 279. suspending_function_async on `setNewsResourceBookmarked` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/OfflineFirstUserDataRepository.kt:45:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setNewsResourceBookmarked' enables non-blocking asynchronous continuation

### 280. suspending_function_async on `setNewsResourceViewed` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/OfflineFirstUserDataRepository.kt:53:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setNewsResourceViewed' enables non-blocking asynchronous continuation

### 281. suspending_function_async on `setThemeBrand` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/OfflineFirstUserDataRepository.kt:56:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setThemeBrand' enables non-blocking asynchronous continuation

### 282. suspending_function_async on `setDarkThemeConfig` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/OfflineFirstUserDataRepository.kt:61:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setDarkThemeConfig' enables non-blocking asynchronous continuation

### 283. suspending_function_async on `setDynamicColorPreference` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/OfflineFirstUserDataRepository.kt:66:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setDynamicColorPreference' enables non-blocking asynchronous continuation

### 284. suspending_function_async on `setShouldHideOnboarding` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/OfflineFirstUserDataRepository.kt:71:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'setShouldHideOnboarding' enables non-blocking asynchronous continuation

### 285. suspending_function_async on `populateFtsData` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/DefaultSearchContentsRepository.kt:47:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'populateFtsData' enables non-blocking asynchronous continuation

### 286. suspending_function_async on `insertOrReplaceRecentSearch` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/DefaultRecentSearchRepository.kt:31:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'insertOrReplaceRecentSearch' enables non-blocking asynchronous continuation

### 287. suspending_function_async on `clearRecentSearches` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/DefaultRecentSearchRepository.kt:45:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'clearRecentSearches' enables non-blocking asynchronous continuation

### 288. suspending_function_async on `syncWith` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/OfflineFirstTopicsRepository.kt:49:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'syncWith' enables non-blocking asynchronous continuation

### 289. suspending_function_async on `subscribe` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/prod/kotlin/com/google/samples/apps/nowinandroid/sync/status/FirebaseSyncSubscriber.kt:30:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'subscribe' enables non-blocking asynchronous continuation

### 290. suspending_function_async on `subscribe` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/status/StubSyncSubscriber.kt:28:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'subscribe' enables non-blocking asynchronous continuation

### 291. suspending_function_async on `subscribe` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/status/SyncSubscriber.kt:23:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'subscribe' enables non-blocking asynchronous continuation

### 292. suspending_function_async on `getForegroundInfo` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/workers/DelegatingWorker.kt:75:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getForegroundInfo' enables non-blocking asynchronous continuation

### 293. suspending_function_async on `doWork` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/workers/DelegatingWorker.kt:78:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'doWork' enables non-blocking asynchronous continuation

### 294. suspending_function_async on `getForegroundInfo` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/workers/SyncWorker.kt:63:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getForegroundInfo' enables non-blocking asynchronous continuation

### 295. suspending_function_async on `doWork` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/workers/SyncWorker.kt:66:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'doWork' enables non-blocking asynchronous continuation

### 296. suspending_function_async on `getChangeListVersions` (85% [VERY_HIGH])
- **Category:** `coroutines_concurrency`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/workers/SyncWorker.kt:89:1`
- **Summary:** Sequential non-blocking asynchronous execution without callback hell.
- **Evidence Trail:**
  - `+85%` (COROUTINES_SUSPEND_FUNCTION): Suspending function 'getChangeListVersions' enables non-blocking asynchronous continuation

### 297. type_safe_builder_dsl on `updateChangeListVersion` (85% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `dsl_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/NiaPreferencesDataSource.kt:169:1`
- **Summary:** Declarative domain builder using higher-order functions with receivers (`T.() -> Unit`).
- **Evidence Trail:**
  - `+85%` (COMPOSE_TYPE_SAFE_BUILDER_DSL): Function 'updateChangeListVersion' implements Type-Safe Builder DSL accepting higher-order lambda with receiver

### 298. type_safe_builder_dsl on `updateChangeListVersions` (85% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `dsl_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/SyncUtilities.kt:31:1`
- **Summary:** Declarative domain builder using higher-order functions with receivers (`T.() -> Unit`).
- **Evidence Trail:**
  - `+85%` (COMPOSE_TYPE_SAFE_BUILDER_DSL): Function 'updateChangeListVersions' implements Type-Safe Builder DSL accepting higher-order lambda with receiver

### 299. compose_declarative_view on `InterestsIcon` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/InterestsItem.kt:103:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'InterestsIcon' acts as a declarative UI component

### 300. compose_declarative_view on `InterestsCardPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/InterestsItem.kt:124:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'InterestsCardPreview' acts as a declarative UI component

### 301. compose_declarative_view on `InterestsCardLongNamePreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/InterestsItem.kt:141:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'InterestsCardLongNamePreview' acts as a declarative UI component

### 302. compose_declarative_view on `InterestsCardLongDescriptionPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/InterestsItem.kt:158:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'InterestsCardLongDescriptionPreview' acts as a declarative UI component

### 303. compose_declarative_view on `InterestsCardWithEmptyDescriptionPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/InterestsItem.kt:176:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'InterestsCardWithEmptyDescriptionPreview' acts as a declarative UI component

### 304. compose_declarative_view on `InterestsCardSelectedPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/InterestsItem.kt:193:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'InterestsCardSelectedPreview' acts as a declarative UI component

### 305. compose_declarative_view on `dateFormatted` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/NewsResourceCard.kt:277:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'dateFormatted' acts as a declarative UI component

### 306. compose_declarative_view on `BookmarkButtonPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/NewsResourceCard.kt:349:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'BookmarkButtonPreview' acts as a declarative UI component

### 307. compose_declarative_view on `BookmarkButtonBookmarkedPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/NewsResourceCard.kt:359:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'BookmarkButtonBookmarkedPreview' acts as a declarative UI component

### 308. compose_declarative_view on `NewsFeedLoadingPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/NewsFeed.kt:127:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NewsFeedLoadingPreview' acts as a declarative UI component

### 309. compose_declarative_view on `rememberMetricsStateHolder` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/JankStatsExtensions.kt:38:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'rememberMetricsStateHolder' acts as a declarative UI component

### 310. compose_declarative_view on `TrackScrollJank` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/JankStatsExtensions.kt:81:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'TrackScrollJank' acts as a declarative UI component

### 311. compose_declarative_view on `NiaTopAppBarExample` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/test/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/TopAppBarScreenshotTests.kt:83:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NiaTopAppBarExample' acts as a declarative UI component

### 312. compose_declarative_view on `NiaIconToggleExample` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/test/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/IconButtonScreenshotTests.kt:62:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NiaIconToggleExample' acts as a declarative UI component

### 313. compose_declarative_view on `NiaTabsExample` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/test/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/TabsScreenshotTests.kt:83:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NiaTabsExample' acts as a declarative UI component

### 314. compose_declarative_view on `dynamicLightColorSchemeWithFallback` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/test/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/ThemeTest.kt:226:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'dynamicLightColorSchemeWithFallback' acts as a declarative UI component

### 315. compose_declarative_view on `dynamicDarkColorSchemeWithFallback` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/test/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/ThemeTest.kt:232:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'dynamicDarkColorSchemeWithFallback' acts as a declarative UI component

### 316. compose_declarative_view on `NiaNavigationBarExample` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/test/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/NavigationScreenshotTests.kt:88:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NiaNavigationBarExample' acts as a declarative UI component

### 317. compose_declarative_view on `NiaLoadingWheelPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/LoadingWheel.kt:154:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NiaLoadingWheelPreview' acts as a declarative UI component

### 318. compose_declarative_view on `NiaOverlayLoadingWheelPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/LoadingWheel.kt:164:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NiaOverlayLoadingWheelPreview' acts as a declarative UI component

### 319. compose_declarative_view on `NiaButtonPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Button.kt:270:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NiaButtonPreview' acts as a declarative UI component

### 320. compose_declarative_view on `NiaOutlinedButtonPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Button.kt:280:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NiaOutlinedButtonPreview' acts as a declarative UI component

### 321. compose_declarative_view on `NiaButtonLeadingIconPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Button.kt:290:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NiaButtonLeadingIconPreview' acts as a declarative UI component

### 322. compose_declarative_view on `ViewTogglePreviewExpanded` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/ViewToggle.kt:114:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'ViewTogglePreviewExpanded' acts as a declarative UI component

### 323. compose_declarative_view on `ViewTogglePreviewCompact` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/ViewToggle.kt:129:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'ViewTogglePreviewCompact' acts as a declarative UI component

### 324. compose_declarative_view on `NiaTopAppBarPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/TopAppBar.kt:80:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NiaTopAppBarPreview' acts as a declarative UI component

### 325. compose_declarative_view on `TagPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Tag.kt:66:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'TagPreview' acts as a declarative UI component

### 326. compose_declarative_view on `NiaNavigationBarPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Navigation.kt:268:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NiaNavigationBarPreview' acts as a declarative UI component

### 327. compose_declarative_view on `NiaNavigationRailPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Navigation.kt:308:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NiaNavigationRailPreview' acts as a declarative UI component

### 328. compose_declarative_view on `navigationContentColor` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Navigation.kt:351:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'navigationContentColor' acts as a declarative UI component

### 329. compose_declarative_view on `navigationSelectedItemColor` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Navigation.kt:354:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'navigationSelectedItemColor' acts as a declarative UI component

### 330. compose_declarative_view on `navigationIndicatorColor` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Navigation.kt:357:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'navigationIndicatorColor' acts as a declarative UI component

### 331. compose_declarative_view on `TabsPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Tabs.kt:106:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'TabsPreview' acts as a declarative UI component

### 332. compose_declarative_view on `IconButtonPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/IconButton.kt:76:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'IconButtonPreview' acts as a declarative UI component

### 333. compose_declarative_view on `IconButtonPreviewUnchecked` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/IconButton.kt:99:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'IconButtonPreviewUnchecked' acts as a declarative UI component

### 334. compose_declarative_view on `BackgroundDefault` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Background.kt:152:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'BackgroundDefault' acts as a declarative UI component

### 335. compose_declarative_view on `BackgroundDynamic` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Background.kt:160:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'BackgroundDynamic' acts as a declarative UI component

### 336. compose_declarative_view on `BackgroundAndroid` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Background.kt:168:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'BackgroundAndroid' acts as a declarative UI component

### 337. compose_declarative_view on `GradientBackgroundDefault` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Background.kt:176:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'GradientBackgroundDefault' acts as a declarative UI component

### 338. compose_declarative_view on `GradientBackgroundDynamic` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Background.kt:184:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'GradientBackgroundDynamic' acts as a declarative UI component

### 339. compose_declarative_view on `GradientBackgroundAndroid` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Background.kt:192:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'GradientBackgroundAndroid' acts as a declarative UI component

### 340. compose_declarative_view on `ChipPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Chip.kt:111:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'ChipPreview' acts as a declarative UI component

### 341. compose_declarative_view on `Content` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/DeviceConfigurationOverrideWindowInsets.kt:42:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'Content' acts as a declarative UI component

### 342. compose_declarative_view on `toInsets` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/SnackbarInsetsScreenshotTests.kt:327:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'toInsets' acts as a declarative UI component

### 343. compose_declarative_view on `NavigationTrackingSideEffect` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/ui/NiaAppState.kt:114:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NavigationTrackingSideEffect' acts as a declarative UI component

### 344. compose_declarative_view on `NiaCatalog` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app-nia-catalog/src/main/kotlin/com/google/samples/apps/niacatalog/ui/Catalog.kt:60:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NiaCatalog' acts as a declarative UI component

### 345. compose_declarative_view on `SettingsDialogSectionTitle` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/settings/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/settings/impl/SettingsDialog.kt:217:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'SettingsDialogSectionTitle' acts as a declarative UI component

### 346. compose_declarative_view on `LinksPanel` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/settings/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/settings/impl/SettingsDialog.kt:253:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'LinksPanel' acts as a declarative UI component

### 347. compose_declarative_view on `PreviewSettingsDialog` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/settings/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/settings/impl/SettingsDialog.kt:290:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'PreviewSettingsDialog' acts as a declarative UI component

### 348. compose_declarative_view on `PreviewSettingsDialogLoading` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/settings/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/settings/impl/SettingsDialog.kt:310:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'PreviewSettingsDialogLoading' acts as a declarative UI component

### 349. compose_declarative_view on `ForYouScreenTopicSelection` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/test/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/ForYouScreenScreenshotTests.kt:165:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'ForYouScreenTopicSelection' acts as a declarative UI component

### 350. compose_declarative_view on `ForYouScreenPopulatedAndLoading` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/test/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/ForYouScreenScreenshotTests.kt:190:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'ForYouScreenPopulatedAndLoading' acts as a declarative UI component

### 351. compose_declarative_view on `NotificationPermissionEffect` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/ForYouScreen.kt:449:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'NotificationPermissionEffect' acts as a declarative UI component

### 352. compose_declarative_view on `ForYouScreenLoading` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/ForYouScreen.kt:581:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'ForYouScreenLoading' acts as a declarative UI component

### 353. compose_declarative_view on `TopicHeader` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/impl/TopicScreen.kt:207:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'TopicHeader' acts as a declarative UI component

### 354. compose_declarative_view on `TopicBodyPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/impl/TopicScreen.kt:260:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'TopicBodyPreview' acts as a declarative UI component

### 355. compose_declarative_view on `TopicScreenLoading` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/impl/TopicScreen.kt:343:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'TopicScreenLoading' acts as a declarative UI component

### 356. compose_declarative_view on `SearchNotReadyBody` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchScreen.kt:270:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'SearchNotReadyBody' acts as a declarative UI component

### 357. compose_declarative_view on `SearchToolbarPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchScreen.kt:554:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'SearchToolbarPreview' acts as a declarative UI component

### 358. compose_declarative_view on `EmptySearchResultColumnPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchScreen.kt:567:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'EmptySearchResultColumnPreview' acts as a declarative UI component

### 359. compose_declarative_view on `RecentSearchesBodyPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchScreen.kt:578:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'RecentSearchesBodyPreview' acts as a declarative UI component

### 360. compose_declarative_view on `SearchNotReadyBodyPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchScreen.kt:590:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'SearchNotReadyBodyPreview' acts as a declarative UI component

### 361. compose_declarative_view on `LoadingState` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/bookmarks/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/bookmarks/impl/BookmarksScreen.kt:153:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'LoadingState' acts as a declarative UI component

### 362. compose_declarative_view on `EmptyState` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/bookmarks/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/bookmarks/impl/BookmarksScreen.kt:220:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'EmptyState' acts as a declarative UI component

### 363. compose_declarative_view on `LoadingStatePreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/bookmarks/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/bookmarks/impl/BookmarksScreen.kt:260:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'LoadingStatePreview' acts as a declarative UI component

### 364. compose_declarative_view on `EmptyStatePreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/bookmarks/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/bookmarks/impl/BookmarksScreen.kt:284:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'EmptyStatePreview' acts as a declarative UI component

### 365. compose_declarative_view on `InterestsScreen` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/feature/interests/impl/InterestsScreenTest.kt:110:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'InterestsScreen' acts as a declarative UI component

### 366. compose_declarative_view on `TestNavDisplay` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/test/kotlin/com/google/samples/apps/nowinandroid/interests/impl/InterestsListDetailScreenTest.kt:110:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'TestNavDisplay' acts as a declarative UI component

### 367. compose_declarative_view on `InterestsDetailPlaceholder` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/impl/InterestsDetailPlaceholder.kt:39:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'InterestsDetailPlaceholder' acts as a declarative UI component

### 368. compose_declarative_view on `TopicDetailPlaceholderPreview` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/impl/InterestsDetailPlaceholder.kt:68:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'TopicDetailPlaceholderPreview' acts as a declarative UI component

### 369. compose_declarative_view on `InterestsEmptyScreen` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/impl/InterestsScreen.kt:93:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'InterestsEmptyScreen' acts as a declarative UI component

### 370. compose_declarative_view on `InterestsScreenLoading` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/impl/InterestsScreen.kt:119:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'InterestsScreenLoading' acts as a declarative UI component

### 371. compose_declarative_view on `InterestsScreenEmpty` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `composable_view`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/impl/InterestsScreen.kt:133:1`
- **Summary:** Declarative UI component transforming data state into reactive UI trees.
- **Evidence Trail:**
  - `+95%` (COMPOSE_DECLARATIVE_VIEW): Composable function 'InterestsScreenEmpty' acts as a declarative UI component

### 372. remember_mutable_state on `rememberMetricsStateHolder` (90% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/JankStatsExtensions.kt:38:1`
- **Summary:** Recomposition-scoped observable state within Jetpack Compose functions.
- **Evidence Trail:**
  - `+90%` (COMPOSE_REMEMBER_MUTABLE_STATE): Function 'rememberMetricsStateHolder' preserves observable UI state across recompositions using remember

### 373. remember_mutable_state on `niaAppState_currentDestination` (90% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/NiaAppStateTest.kt:78:1`
- **Summary:** Recomposition-scoped observable state within Jetpack Compose functions.
- **Evidence Trail:**
  - `+90%` (COMPOSE_REMEMBER_MUTABLE_STATE): Function 'niaAppState_currentDestination' preserves observable UI state across recompositions using remember

### 374. remember_mutable_state on `NiaCatalog` (90% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app-nia-catalog/src/main/kotlin/com/google/samples/apps/niacatalog/ui/Catalog.kt:60:1`
- **Summary:** Recomposition-scoped observable state within Jetpack Compose functions.
- **Evidence Trail:**
  - `+90%` (COMPOSE_REMEMBER_MUTABLE_STATE): Function 'NiaCatalog' preserves observable UI state across recompositions using remember

### 375. view_model_state_holder on `MainActivityViewModel` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/MainActivityViewModel.kt:35:1`
- **Summary:** Architecture component retaining and coordinating UI state across configuration changes.
- **Evidence Trail:**
  - `+95%` (COMPOSE_VIEWMODEL_STATE_HOLDER): Class 'MainActivityViewModel' implements ViewModel architectural state holder

### 376. view_model_state_holder on `SettingsViewModel` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/settings/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/settings/impl/SettingsViewModel.kt:36:1`
- **Summary:** Architecture component retaining and coordinating UI state across configuration changes.
- **Evidence Trail:**
  - `+95%` (COMPOSE_VIEWMODEL_STATE_HOLDER): Class 'SettingsViewModel' implements ViewModel architectural state holder

### 377. view_model_state_holder on `ForYouViewModel` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/ForYouViewModel.kt:45:1`
- **Summary:** Architecture component retaining and coordinating UI state across configuration changes.
- **Evidence Trail:**
  - `+95%` (COMPOSE_VIEWMODEL_STATE_HOLDER): Class 'ForYouViewModel' implements ViewModel architectural state holder

### 378. view_model_state_holder on `TopicViewModel` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/impl/TopicViewModel.kt:43:1`
- **Summary:** Architecture component retaining and coordinating UI state across configuration changes.
- **Evidence Trail:**
  - `+95%` (COMPOSE_VIEWMODEL_STATE_HOLDER): Class 'TopicViewModel' implements ViewModel architectural state holder

### 379. view_model_state_holder on `SearchViewModel` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchViewModel.kt:43:1`
- **Summary:** Architecture component retaining and coordinating UI state across configuration changes.
- **Evidence Trail:**
  - `+95%` (COMPOSE_VIEWMODEL_STATE_HOLDER): Class 'SearchViewModel' implements ViewModel architectural state holder

### 380. view_model_state_holder on `BookmarksViewModel` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/bookmarks/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/bookmarks/impl/BookmarksViewModel.kt:39:1`
- **Summary:** Architecture component retaining and coordinating UI state across configuration changes.
- **Evidence Trail:**
  - `+95%` (COMPOSE_VIEWMODEL_STATE_HOLDER): Class 'BookmarksViewModel' implements ViewModel architectural state holder

### 381. view_model_state_holder on `InterestsViewModel` (95% [VERY_HIGH])
- **Category:** `compose_dsl`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/impl/InterestsViewModel.kt:38:1`
- **Summary:** Architecture component retaining and coordinating UI state across configuration changes.
- **Evidence Trail:**
  - `+95%` (COMPOSE_VIEWMODEL_STATE_HOLDER): Class 'InterestsViewModel' implements ViewModel architectural state holder

### 382. singleton_object_declaration on `PreviewParameterData` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/UserNewsResourcePreviewParameterProvider.kt:43:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'PreviewParameterData' provides language-level thread-safe Singleton

### 383. singleton_object_declaration on `DatabaseMigrations` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/DatabaseMigrations.kt:31:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'DatabaseMigrations' provides language-level thread-safe Singleton

### 384. singleton_object_declaration on `DaosModule` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/di/DaosModule.kt:32:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'DaosModule' provides language-level thread-safe Singleton

### 385. singleton_object_declaration on `DatabaseModule` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/di/DatabaseModule.kt:31:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'DatabaseModule' provides language-level thread-safe Singleton

### 386. singleton_object_declaration on `NiaButtonDefaults` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Button.kt:305:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'NiaButtonDefaults' provides language-level thread-safe Singleton

### 387. singleton_object_declaration on `NiaViewToggleDefaults` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/ViewToggle.kt:145:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'NiaViewToggleDefaults' provides language-level thread-safe Singleton

### 388. singleton_object_declaration on `NiaTagDefaults` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Tag.kt:77:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'NiaTagDefaults' provides language-level thread-safe Singleton

### 389. singleton_object_declaration on `NiaNavigationDefaults` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Navigation.kt:349:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'NiaNavigationDefaults' provides language-level thread-safe Singleton

### 390. singleton_object_declaration on `NiaTabDefaults` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Tabs.kt:121:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'NiaTabDefaults' provides language-level thread-safe Singleton

### 391. singleton_object_declaration on `NiaIconButtonDefaults` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/IconButton.kt:123:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'NiaIconButtonDefaults' provides language-level thread-safe Singleton

### 392. singleton_object_declaration on `NiaChipDefaults` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/Chip.kt:124:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'NiaChipDefaults' provides language-level thread-safe Singleton

### 393. singleton_object_declaration on `NiaIcons` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/icon/NiaIcons.kt:42:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'NiaIcons' provides language-level thread-safe Singleton

### 394. singleton_object_declaration on `JvmUnitTestDemoAssetManager` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/JvmUnitTestDemoAssetManager.kt:28:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'JvmUnitTestDemoAssetManager' provides language-level thread-safe Singleton

### 395. singleton_object_declaration on `NetworkModule` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/di/NetworkModule.kt:39:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'NetworkModule' provides language-level thread-safe Singleton

### 396. singleton_object_declaration on `TestFirstTopLevelKey` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/navigation/src/test/kotlin/com/google/samples/apps/nowinandroid/core/navigation/NavigatorTest.kt:26:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'TestFirstTopLevelKey' provides language-level thread-safe Singleton

### 397. singleton_object_declaration on `TestSecondTopLevelKey` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/navigation/src/test/kotlin/com/google/samples/apps/nowinandroid/core/navigation/NavigatorTest.kt:27:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'TestSecondTopLevelKey' provides language-level thread-safe Singleton

### 398. singleton_object_declaration on `TestThirdTopLevelKey` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/navigation/src/test/kotlin/com/google/samples/apps/nowinandroid/core/navigation/NavigatorTest.kt:28:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'TestThirdTopLevelKey' provides language-level thread-safe Singleton

### 399. singleton_object_declaration on `TestKeyFirst` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/navigation/src/test/kotlin/com/google/samples/apps/nowinandroid/core/navigation/NavigatorTest.kt:29:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'TestKeyFirst' provides language-level thread-safe Singleton

### 400. singleton_object_declaration on `TestKeySecond` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/navigation/src/test/kotlin/com/google/samples/apps/nowinandroid/core/navigation/NavigatorTest.kt:30:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'TestKeySecond' provides language-level thread-safe Singleton

### 401. singleton_object_declaration on `TestDispatcherModule` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/di/TestDispatcherModule.kt:29:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'TestDispatcherModule' provides language-level thread-safe Singleton

### 402. singleton_object_declaration on `TestDispatchersModule` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/di/TestDispatchersModule.kt:35:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'TestDispatchersModule' provides language-level thread-safe Singleton

### 403. singleton_object_declaration on `TestDataStoreModule` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/test/TestDataStoreModule.kt:34:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'TestDataStoreModule' provides language-level thread-safe Singleton

### 404. singleton_object_declaration on `IntToStringIdsMigration` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/IntToStringIdsMigration.kt:24:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'IntToStringIdsMigration' provides language-level thread-safe Singleton

### 405. singleton_object_declaration on `ListToMapMigration` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/ListToMapMigration.kt:24:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'ListToMapMigration' provides language-level thread-safe Singleton

### 406. singleton_object_declaration on `DataStoreModule` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/di/DataStoreModule.kt:40:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'DataStoreModule' provides language-level thread-safe Singleton

### 407. singleton_object_declaration on `CoroutineScopesModule` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/common/src/main/kotlin/com/google/samples/apps/nowinandroid/core/common/network/di/CoroutineScopesModule.kt:37:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'CoroutineScopesModule' provides language-level thread-safe Singleton

### 408. singleton_object_declaration on `DispatchersModule` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/common/src/main/kotlin/com/google/samples/apps/nowinandroid/core/common/network/di/DispatchersModule.kt:31:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'DispatchersModule' provides language-level thread-safe Singleton

### 409. singleton_object_declaration on `JankStatsModule` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/di/JankStatsModule.kt:31:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'JankStatsModule' provides language-level thread-safe Singleton

### 410. singleton_object_declaration on `ForYouNavKey` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/api/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/api/navigation/ForYouNavKey.kt:23:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'ForYouNavKey' provides language-level thread-safe Singleton

### 411. singleton_object_declaration on `SearchNavKey` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/api/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/api/navigation/SearchNavKey.kt:23:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'SearchNavKey' provides language-level thread-safe Singleton

### 412. singleton_object_declaration on `BookmarksNavKey` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/bookmarks/api/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/bookmarks/api/navigation/BookmarksNavKey.kt:23:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'BookmarksNavKey' provides language-level thread-safe Singleton

### 413. singleton_object_declaration on `Sync` (95% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `object`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/initializers/SyncInitializer.kt:24:1`
- **Summary:** Thread-safe, lazy language-level Singleton via `object` declaration.
- **Evidence Trail:**
  - `+95%` (CREATIONAL_SINGLETON_OBJECT): Object declaration 'Sync' provides language-level thread-safe Singleton

### 414. factory_method on `DesignSystemDetector.createUastHandler` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/lint/src/main/kotlin/com/google/samples/apps/nowinandroid/lint/designsystem/DesignSystemDetector.kt:42:1`
- **Summary:** Static or interface factory method instantiating polymorphic types (`create...`, `make...`).
- **Evidence Trail:**
  - `+85%` (CREATIONAL_FACTORY_METHOD): Method 'createUastHandler' on 'DesignSystemDetector' encapsulates instance instantiation as a Factory Method

### 415. prototype_data_copy on `PopulatedNewsResource` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/model/PopulatedNewsResource.kt:27:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'PopulatedNewsResource' implements Prototype pattern for instance replication and value transformation

### 416. prototype_data_copy on `TopicEntity` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/model/TopicEntity.kt:31:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'TopicEntity' implements Prototype pattern for instance replication and value transformation

### 417. prototype_data_copy on `RecentSearchQueryEntity` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/model/RecentSearchQueryEntity.kt:30:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'RecentSearchQueryEntity' implements Prototype pattern for instance replication and value transformation

### 418. prototype_data_copy on `NewsResourceFtsEntity` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/model/NewsResourceFtsEntity.kt:28:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'NewsResourceFtsEntity' implements Prototype pattern for instance replication and value transformation

### 419. prototype_data_copy on `NewsResourceTopicCrossRef` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/model/NewsResourceTopicCrossRef.kt:49:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'NewsResourceTopicCrossRef' implements Prototype pattern for instance replication and value transformation

### 420. prototype_data_copy on `NewsResourceEntity` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/model/NewsResourceEntity.kt:31:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'NewsResourceEntity' implements Prototype pattern for instance replication and value transformation

### 421. prototype_data_copy on `TopicFtsEntity` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/database/src/main/kotlin/com/google/samples/apps/nowinandroid/core/database/model/TopicFtsEntity.kt:28:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'TopicFtsEntity' implements Prototype pattern for instance replication and value transformation

### 422. prototype_data_copy on `ScrollThumbElement` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/AppScrollbars.kt:179:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'ScrollThumbElement' implements Prototype pattern for instance replication and value transformation

### 423. prototype_data_copy on `TintTheme` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/theme/Tint.kt:27:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'TintTheme' implements Prototype pattern for instance replication and value transformation

### 424. prototype_data_copy on `BackgroundTheme` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/theme/Background.kt:28:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'BackgroundTheme' implements Prototype pattern for instance replication and value transformation

### 425. prototype_data_copy on `GradientColors` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/theme/Gradient.kt:31:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'GradientColors' implements Prototype pattern for instance replication and value transformation

### 426. prototype_data_copy on `TestDeviceSpecs` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/screenshot-testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/util/ScreenshotHelper.kt:271:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'TestDeviceSpecs' implements Prototype pattern for instance replication and value transformation

### 427. prototype_data_copy on `NetworkResponse` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/retrofit/RetrofitNiaNetwork.kt:67:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'NetworkResponse' implements Prototype pattern for instance replication and value transformation

### 428. prototype_data_copy on `NetworkNewsResource` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/model/NetworkNewsResource.kt:29:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'NetworkNewsResource' implements Prototype pattern for instance replication and value transformation

### 429. prototype_data_copy on `NetworkTopic` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/model/NetworkTopic.kt:26:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'NetworkTopic' implements Prototype pattern for instance replication and value transformation

### 430. prototype_data_copy on `NetworkChangeList` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/src/main/kotlin/com/google/samples/apps/nowinandroid/core/network/model/NetworkChangeList.kt:28:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'NetworkChangeList' implements Prototype pattern for instance replication and value transformation

### 431. prototype_data_copy on `ChangeListVersions` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/datastore/src/main/kotlin/com/google/samples/apps/nowinandroid/core/datastore/ChangeListVersions.kt:22:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'ChangeListVersions' implements Prototype pattern for instance replication and value transformation

### 432. prototype_data_copy on `UserData` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/model/src/main/kotlin/com/google/samples/apps/nowinandroid/core/model/data/UserData.kt:22:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'UserData' implements Prototype pattern for instance replication and value transformation

### 433. prototype_data_copy on `Topic` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/model/src/main/kotlin/com/google/samples/apps/nowinandroid/core/model/data/Topic.kt:22:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'Topic' implements Prototype pattern for instance replication and value transformation

### 434. prototype_data_copy on `SearchResult` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/model/src/main/kotlin/com/google/samples/apps/nowinandroid/core/model/data/SearchResult.kt:20:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'SearchResult' implements Prototype pattern for instance replication and value transformation

### 435. prototype_data_copy on `UserSearchResult` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/model/src/main/kotlin/com/google/samples/apps/nowinandroid/core/model/data/UserSearchResult.kt:23:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'UserSearchResult' implements Prototype pattern for instance replication and value transformation

### 436. prototype_data_copy on `NewsResource` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/model/src/main/kotlin/com/google/samples/apps/nowinandroid/core/model/data/NewsResource.kt:24:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'NewsResource' implements Prototype pattern for instance replication and value transformation

### 437. prototype_data_copy on `FollowableTopic` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/model/src/main/kotlin/com/google/samples/apps/nowinandroid/core/model/data/FollowableTopic.kt:23:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'FollowableTopic' implements Prototype pattern for instance replication and value transformation

### 438. prototype_data_copy on `UserNewsResource` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/model/src/main/kotlin/com/google/samples/apps/nowinandroid/core/model/data/UserNewsResource.kt:25:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'UserNewsResource' implements Prototype pattern for instance replication and value transformation

### 439. prototype_data_copy on `NewsResourceQuery` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/NewsRepository.kt:26:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'NewsResourceQuery' implements Prototype pattern for instance replication and value transformation

### 440. prototype_data_copy on `RecentSearchQuery` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/model/RecentSearchQuery.kt:23:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'RecentSearchQuery' implements Prototype pattern for instance replication and value transformation

### 441. prototype_data_copy on `AnalyticsEvent` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/analytics/src/main/kotlin/com/google/samples/apps/nowinandroid/core/analytics/AnalyticsEvent.kt:29:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'AnalyticsEvent' implements Prototype pattern for instance replication and value transformation

### 442. prototype_data_copy on `ThemeSettings` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/MainActivity.kt:186:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'ThemeSettings' implements Prototype pattern for instance replication and value transformation

### 443. prototype_data_copy on `TopLevelNavItem` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/navigation/TopLevelNavItem.kt:41:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'TopLevelNavItem' implements Prototype pattern for instance replication and value transformation

### 444. prototype_data_copy on `DeviceConfig` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/com/google/samples/apps/nowinandroid/GradleManagedDevices.kt:60:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'DeviceConfig' implements Prototype pattern for instance replication and value transformation

### 445. prototype_data_copy on `UserEditableSettings` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/settings/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/settings/impl/SettingsViewModel.kt:78:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'UserEditableSettings' implements Prototype pattern for instance replication and value transformation

### 446. prototype_data_copy on `TopicNavKey` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/api/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/api/navigation/TopicNavKey.kt:24:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'TopicNavKey' implements Prototype pattern for instance replication and value transformation

### 447. prototype_data_copy on `InterestsNavKey` (85% [VERY_HIGH])
- **Category:** `creational`
- **Target Kind:** `data_class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/api/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/api/navigation/InterestsNavKey.kt:23:1`
- **Summary:** Immutable instance replication and value transformation via `copy()` or `Cloneable`.
- **Evidence Trail:**
  - `+85%` (CREATIONAL_PROTOTYPE_DATA_COPY): Type 'InterestsNavKey' implements Prototype pattern for instance replication and value transformation

### 448. composite_view_tree on `CompositeUserNewsResourceRepositoryTest` (85% [VERY_HIGH])
- **Category:** `structural`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/test/kotlin/com/google/samples/apps/nowinandroid/core/data/CompositeUserNewsResourceRepositoryTest.kt:33:1`
- **Summary:** Hierarchical composite tree treating individual and grouped elements uniformly.
- **Evidence Trail:**
  - `+85%` (STRUCTURAL_COMPOSITE_TREE): Class 'CompositeUserNewsResourceRepositoryTest' implements Composite pattern hosting recursive child component hierarchy

### 449. composite_view_tree on `CompositeUserNewsResourceRepository` (85% [VERY_HIGH])
- **Category:** `structural`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/CompositeUserNewsResourceRepository.kt:33:1`
- **Summary:** Hierarchical composite tree treating individual and grouped elements uniformly.
- **Evidence Trail:**
  - `+85%` (STRUCTURAL_COMPOSITE_TREE): Class 'CompositeUserNewsResourceRepository' implements Composite pattern hosting recursive child component hierarchy

### 450. facade_coordinator on `CompositeUserNewsResourceRepository` (80% [HIGH])
- **Category:** `structural`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/CompositeUserNewsResourceRepository.kt:33:1`
- **Summary:** Unified coordinator orchestrating multiple subsystem repositories, use cases, or clients.
- **Evidence Trail:**
  - `+80%` (STRUCTURAL_FACADE_COORDINATOR): Class 'CompositeUserNewsResourceRepository' coordinates 2 subsystem dependencies as a unified Facade

### 451. facade_coordinator on `GetSearchContentsUseCase` (80% [HIGH])
- **Category:** `structural`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/domain/src/main/kotlin/com/google/samples/apps/nowinandroid/core/domain/GetSearchContentsUseCase.kt:33:1`
- **Summary:** Unified coordinator orchestrating multiple subsystem repositories, use cases, or clients.
- **Evidence Trail:**
  - `+80%` (STRUCTURAL_FACADE_COORDINATOR): Class 'GetSearchContentsUseCase' coordinates 2 subsystem dependencies as a unified Facade

### 452. facade_coordinator on `GetFollowableTopicsUseCase` (80% [HIGH])
- **Category:** `structural`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/domain/src/main/kotlin/com/google/samples/apps/nowinandroid/core/domain/GetFollowableTopicsUseCase.kt:31:1`
- **Summary:** Unified coordinator orchestrating multiple subsystem repositories, use cases, or clients.
- **Evidence Trail:**
  - `+80%` (STRUCTURAL_FACADE_COORDINATOR): Class 'GetFollowableTopicsUseCase' coordinates 2 subsystem dependencies as a unified Facade

### 453. facade_coordinator on `NavigationTest` (80% [HIGH])
- **Category:** `structural`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/ui/NavigationTest.kt:62:1`
- **Summary:** Unified coordinator orchestrating multiple subsystem repositories, use cases, or clients.
- **Evidence Trail:**
  - `+80%` (STRUCTURAL_FACADE_COORDINATOR): Class 'NavigationTest' coordinates 2 subsystem dependencies as a unified Facade

### 454. facade_coordinator on `NiaAppScreenSizesScreenshotTests` (80% [HIGH])
- **Category:** `structural`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/NiaAppScreenSizesScreenshotTests.kt:66:1`
- **Summary:** Unified coordinator orchestrating multiple subsystem repositories, use cases, or clients.
- **Evidence Trail:**
  - `+80%` (STRUCTURAL_FACADE_COORDINATOR): Class 'NiaAppScreenSizesScreenshotTests' coordinates 3 subsystem dependencies as a unified Facade

### 455. facade_coordinator on `SnackbarScreenshotTests` (80% [HIGH])
- **Category:** `structural`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/SnackbarScreenshotTests.kt:73:1`
- **Summary:** Unified coordinator orchestrating multiple subsystem repositories, use cases, or clients.
- **Evidence Trail:**
  - `+80%` (STRUCTURAL_FACADE_COORDINATOR): Class 'SnackbarScreenshotTests' coordinates 3 subsystem dependencies as a unified Facade

### 456. facade_coordinator on `SnackbarInsetsScreenshotTests` (80% [HIGH])
- **Category:** `structural`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/SnackbarInsetsScreenshotTests.kt:100:1`
- **Summary:** Unified coordinator orchestrating multiple subsystem repositories, use cases, or clients.
- **Evidence Trail:**
  - `+80%` (STRUCTURAL_FACADE_COORDINATOR): Class 'SnackbarInsetsScreenshotTests' coordinates 3 subsystem dependencies as a unified Facade

### 457. facade_coordinator on `SearchViewModel` (80% [HIGH])
- **Category:** `structural`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchViewModel.kt:43:1`
- **Summary:** Unified coordinator orchestrating multiple subsystem repositories, use cases, or clients.
- **Evidence Trail:**
  - `+80%` (STRUCTURAL_FACADE_COORDINATOR): Class 'SearchViewModel' coordinates 3 subsystem dependencies as a unified Facade

### 458. facade_coordinator on `SyncWorker` (80% [HIGH])
- **Category:** `structural`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/workers/SyncWorker.kt:51:1`
- **Summary:** Unified coordinator orchestrating multiple subsystem repositories, use cases, or clients.
- **Evidence Trail:**
  - `+80%` (STRUCTURAL_FACADE_COORDINATOR): Class 'SyncWorker' coordinates 3 subsystem dependencies as a unified Facade

### 459. flyweight_pool_cache on `TestRecentSearchRepository` (85% [VERY_HIGH])
- **Category:** `structural`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestRecentSearchRepository.kt:24:1`
- **Summary:** Sharing fine-grained immutable instances via factory caching to minimize memory consumption.
- **Evidence Trail:**
  - `+85%` (STRUCTURAL_FLYWEIGHT_CACHE): Type 'TestRecentSearchRepository' shares fine-grained instances via Flyweight pooling cache

### 460. flyweight_pool_cache on `TestSearchContentsRepository` (85% [VERY_HIGH])
- **Category:** `structural`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestSearchContentsRepository.kt:29:1`
- **Summary:** Sharing fine-grained immutable instances via factory caching to minimize memory consumption.
- **Evidence Trail:**
  - `+85%` (STRUCTURAL_FLYWEIGHT_CACHE): Type 'TestSearchContentsRepository' shares fine-grained instances via Flyweight pooling cache

### 461. mediator_coordinator on `NavigatorTest` (85% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/navigation/src/test/kotlin/com/google/samples/apps/nowinandroid/core/navigation/NavigatorTest.kt:32:1`
- **Summary:** Centralized coordinator decoupling components and managing communication flows.
- **Evidence Trail:**
  - `+85%` (BEHAVIORAL_MEDIATOR_COORDINATOR): Class 'NavigatorTest' acts as Mediator / Coordinator decoupling components and managing navigation flows

### 462. mediator_coordinator on `Navigator` (85% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/navigation/src/main/kotlin/com/google/samples/apps/nowinandroid/core/navigation/Navigator.kt:26:1`
- **Summary:** Centralized coordinator decoupling components and managing communication flows.
- **Evidence Trail:**
  - `+85%` (BEHAVIORAL_MEDIATOR_COORDINATOR): Class 'Navigator' acts as Mediator / Coordinator decoupling components and managing navigation flows

### 463. observer_flow_published on `DefaultZoneIdTimeZoneMonitor` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/DefaultZoneIdTimeZoneMonitor.kt:25:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'DefaultZoneIdTimeZoneMonitor' acts as Reactive Observer Subject publishing 1 stream(s)

### 464. observer_flow_published on `AlwaysOnlineNetworkMonitor` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/test/AlwaysOnlineNetworkMonitor.kt:24:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'AlwaysOnlineNetworkMonitor' acts as Reactive Observer Subject publishing 1 stream(s)

### 465. observer_flow_published on `TestUserDataRepository` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/repository/TestUserDataRepository.kt:38:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'TestUserDataRepository' acts as Reactive Observer Subject publishing 1 stream(s)

### 466. observer_flow_published on `TestTimeZoneMonitor` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/util/TestTimeZoneMonitor.kt:24:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'TestTimeZoneMonitor' acts as Reactive Observer Subject publishing 1 stream(s)

### 467. observer_flow_published on `TestNetworkMonitor` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/util/TestNetworkMonitor.kt:23:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'TestNetworkMonitor' acts as Reactive Observer Subject publishing 1 stream(s)

### 468. observer_flow_published on `TestSyncManager` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/util/TestSyncManager.kt:23:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'TestSyncManager' acts as Reactive Observer Subject publishing 1 stream(s)

### 469. observer_flow_published on `UserDataRepository` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/UserDataRepository.kt:24:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'UserDataRepository' acts as Reactive Observer Subject publishing 1 stream(s)

### 470. observer_flow_published on `SyncManager` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/util/SyncManager.kt:24:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'SyncManager' acts as Reactive Observer Subject publishing 1 stream(s)

### 471. observer_flow_published on `ConnectivityManagerNetworkMonitor` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/util/ConnectivityManagerNetworkMonitor.kt:39:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'ConnectivityManagerNetworkMonitor' acts as Reactive Observer Subject publishing 1 stream(s)

### 472. observer_flow_published on `NetworkMonitor` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/util/NetworkMonitor.kt:24:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'NetworkMonitor' acts as Reactive Observer Subject publishing 1 stream(s)

### 473. observer_flow_published on `TimeZoneMonitor` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/util/TimeZoneMonitor.kt:51:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'TimeZoneMonitor' acts as Reactive Observer Subject publishing 1 stream(s)

### 474. observer_flow_published on `MainActivityViewModel` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/MainActivityViewModel.kt:35:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'MainActivityViewModel' acts as Reactive Observer Subject publishing 1 stream(s)

### 475. observer_flow_published on `TopicViewModel` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/impl/TopicViewModel.kt:43:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'TopicViewModel' acts as Reactive Observer Subject publishing 2 stream(s)

### 476. observer_flow_published on `InterestsViewModel` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/impl/InterestsViewModel.kt:38:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'InterestsViewModel' acts as Reactive Observer Subject publishing 1 stream(s)

### 477. observer_flow_published on `NeverSyncingSyncManager` (90% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/sync-test/src/main/kotlin/com/google/samples/apps/nowinandroid/core/sync/test/NeverSyncingSyncManager.kt:24:1`
- **Summary:** Reactive observer publisher notifying subscribed collectors on state mutations.
- **Evidence Trail:**
  - `+90%` (BEHAVIORAL_OBSERVER_FLOW): Type 'NeverSyncingSyncManager' acts as Reactive Observer Subject publishing 1 stream(s)

### 478. state_sealed_class_fsm on `NewsFeedUiState` (95% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/ui/src/main/kotlin/com/google/samples/apps/nowinandroid/core/ui/NewsFeed.kt:108:1`
- **Summary:** Type-safe finite state machine modeling distinct lifecycle states with payload data.
- **Evidence Trail:**
  - `+95%` (BEHAVIORAL_STATE_SEALED_FSM): Sealed type 'NewsFeedUiState' models type-safe Finite State Machine (FSM) with associated lifecycle states

### 479. state_sealed_class_fsm on `MainActivityUiState` (95% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/main/kotlin/com/google/samples/apps/nowinandroid/MainActivityViewModel.kt:47:1`
- **Summary:** Type-safe finite state machine modeling distinct lifecycle states with payload data.
- **Evidence Trail:**
  - `+95%` (BEHAVIORAL_STATE_SEALED_FSM): Sealed type 'MainActivityUiState' models type-safe Finite State Machine (FSM) with associated lifecycle states

### 480. state_sealed_class_fsm on `SettingsUiState` (95% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/settings/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/settings/impl/SettingsViewModel.kt:84:1`
- **Summary:** Type-safe finite state machine modeling distinct lifecycle states with payload data.
- **Evidence Trail:**
  - `+95%` (BEHAVIORAL_STATE_SEALED_FSM): Sealed type 'SettingsUiState' models type-safe Finite State Machine (FSM) with associated lifecycle states

### 481. state_sealed_class_fsm on `OnboardingUiState` (95% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/OnboardingUiState.kt:24:1`
- **Summary:** Type-safe finite state machine modeling distinct lifecycle states with payload data.
- **Evidence Trail:**
  - `+95%` (BEHAVIORAL_STATE_SEALED_FSM): Sealed type 'OnboardingUiState' models type-safe Finite State Machine (FSM) with associated lifecycle states

### 482. state_sealed_class_fsm on `TopicUiState` (95% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/impl/TopicViewModel.kt:161:1`
- **Summary:** Type-safe finite state machine modeling distinct lifecycle states with payload data.
- **Evidence Trail:**
  - `+95%` (BEHAVIORAL_STATE_SEALED_FSM): Sealed type 'TopicUiState' models type-safe Finite State Machine (FSM) with associated lifecycle states

### 483. state_sealed_class_fsm on `NewsUiState` (95% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/topic/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/topic/impl/TopicViewModel.kt:167:1`
- **Summary:** Type-safe finite state machine modeling distinct lifecycle states with payload data.
- **Evidence Trail:**
  - `+95%` (BEHAVIORAL_STATE_SEALED_FSM): Sealed type 'NewsUiState' models type-safe Finite State Machine (FSM) with associated lifecycle states

### 484. state_sealed_class_fsm on `SearchResultUiState` (95% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchResultUiState.kt:22:1`
- **Summary:** Type-safe finite state machine modeling distinct lifecycle states with payload data.
- **Evidence Trail:**
  - `+95%` (BEHAVIORAL_STATE_SEALED_FSM): Sealed type 'SearchResultUiState' models type-safe Finite State Machine (FSM) with associated lifecycle states

### 485. state_sealed_class_fsm on `RecentSearchQueriesUiState` (95% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/RecentSearchQueriesUiState.kt:21:1`
- **Summary:** Type-safe finite state machine modeling distinct lifecycle states with payload data.
- **Evidence Trail:**
  - `+95%` (BEHAVIORAL_STATE_SEALED_FSM): Sealed type 'RecentSearchQueriesUiState' models type-safe Finite State Machine (FSM) with associated lifecycle states

### 486. state_sealed_class_fsm on `InterestsUiState` (95% [VERY_HIGH])
- **Category:** `behavioral`
- **Target Kind:** `sealed_interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/main/kotlin/com/google/samples/apps/nowinandroid/feature/interests/impl/InterestsViewModel.kt:84:1`
- **Summary:** Type-safe finite state machine modeling distinct lifecycle states with payload data.
- **Evidence Trail:**
  - `+95%` (BEHAVIORAL_STATE_SEALED_FSM): Sealed type 'InterestsUiState' models type-safe Finite State Machine (FSM) with associated lifecycle states

### 487. non_cancellation_exception_swallow on `suspendRunCatching` (88% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `suspend_function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/SyncUtilities.kt:55:1`
- **Summary:** Catching generic `Exception` inside coroutines without rethrowing `CancellationException`, breaking cancellation.
- **Evidence Trail:**
  - `+88%` (HAZARD_CANCELLATION_EXCEPTION_SWALLOWED): Suspending function 'suspendRunCatching' catches generic Exception without rethrowing CancellationException, breaking coroutine cancellation

### 488. force_null_assertion_hazard on `lastOutline!!` (85% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `expression`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/main/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/component/scrollbar/AppScrollbars.kt:200:1`
- **Summary:** Force-null unwrapping with `!!` risking immediate `NullPointerException` at runtime.
- **Evidence Trail:**
  - `+85%` (HAZARD_FORCE_NULL_ASSERTION): Unsafe force-null assertion ('lastOutline!!') risks NullPointerException at runtime

### 489. force_null_assertion_hazard on `buildConfigFields!!` (85% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `expression`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/network/build.gradle.kts:61:1`
- **Summary:** Force-null unwrapping with `!!` risking immediate `NullPointerException` at runtime.
- **Evidence Trail:**
  - `+85%` (HAZARD_FORCE_NULL_ASSERTION): Unsafe force-null assertion ('buildConfigFields!!') risks NullPointerException at runtime

### 490. force_null_assertion_hazard on `)!!` (85% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `expression`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/DeviceConfigurationOverrideWindowInsets.kt:52:1`
- **Summary:** Force-null unwrapping with `!!` risking immediate `NullPointerException` at runtime.
- **Evidence Trail:**
  - `+85%` (HAZARD_FORCE_NULL_ASSERTION): Unsafe force-null assertion (')!!') risks NullPointerException at runtime

### 491. force_null_assertion_hazard on `)!!` (85% [VERY_HIGH])
- **Category:** `resilience`
- **Target Kind:** `expression`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/sync/workers/SyncWorkerTest.kt:58:1`
- **Summary:** Force-null unwrapping with `!!` risking immediate `NullPointerException` at runtime.
- **Evidence Trail:**
  - `+85%` (HAZARD_FORCE_NULL_ASSERTION): Unsafe force-null assertion (')!!') risks NullPointerException at runtime

### 492. force_cast_hazard on `uiState_whenFollowingNewTopic_thenShowUpdatedTopics` (80% [HIGH])
- **Category:** `resilience`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/test/kotlin/com/google/samples/apps/nowinandroid/interests/impl/InterestsViewModelTest.kt:93:1`
- **Summary:** Unsafe type casting with `as` instead of safe cast `as?`, risking `ClassCastException`.
- **Evidence Trail:**
  - `+80%` (HAZARD_UNSAFE_FORCE_CAST): Function 'uiState_whenFollowingNewTopic_thenShowUpdatedTopics' performs unsafe downcast ('as InterestsUiState') without safe cast 'as?'

### 493. force_cast_hazard on `uiState_whenUnfollowingTopics_thenShowUpdatedTopics` (80% [HIGH])
- **Category:** `resilience`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/interests/impl/src/test/kotlin/com/google/samples/apps/nowinandroid/interests/impl/InterestsViewModelTest.kt:121:1`
- **Summary:** Unsafe type casting with `as` instead of safe cast `as?`, risking `ClassCastException`.
- **Evidence Trail:**
  - `+80%` (HAZARD_UNSAFE_FORCE_CAST): Function 'uiState_whenUnfollowingTopics_thenShowUpdatedTopics' performs unsafe downcast ('as InterestsUiState') without safe cast 'as?'

### 494. massive_viewmodel_srp on `ThemeTest` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/designsystem/src/test/kotlin/com/google/samples/apps/nowinandroid/core/designsystem/ThemeTest.kt:60:1`
- **Summary:** Type with excessive responsibilities, methods, or lines of code violating SRP.
- **Evidence Trail:**
  - `+80%` (SRP_MASSIVE_VIEWMODEL): Type 'ThemeTest' is a Massive ViewModel / God Class (240 lines, 16 methods, 33 properties) violating SRP

### 495. massive_viewmodel_srp on `OfflineFirstNewsRepositoryTest` (90% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/test/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/OfflineFirstNewsRepositoryTest.kt:51:1`
- **Summary:** Type with excessive responsibilities, methods, or lines of code violating SRP.
- **Evidence Trail:**
  - `+90%` (SRP_MASSIVE_VIEWMODEL): Type 'OfflineFirstNewsRepositoryTest' is a Massive ViewModel / God Class (328 lines, 12 methods, 23 properties) violating SRP

### 496. massive_viewmodel_srp on `NavigationTest` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/app/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/ui/NavigationTest.kt:62:1`
- **Summary:** Type with excessive responsibilities, methods, or lines of code violating SRP.
- **Evidence Trail:**
  - `+80%` (SRP_MASSIVE_VIEWMODEL): Type 'NavigationTest' is a Massive ViewModel / God Class (264 lines, 13 methods, 18 properties) violating SRP

### 497. massive_viewmodel_srp on `ForYouScreenTest` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/ForYouScreenTest.kt:39:1`
- **Summary:** Type with excessive responsibilities, methods, or lines of code violating SRP.
- **Evidence Trail:**
  - `+80%` (SRP_MASSIVE_VIEWMODEL): Type 'ForYouScreenTest' is a Massive ViewModel / God Class (257 lines, 7 methods, 4 properties) violating SRP

### 498. massive_viewmodel_srp on `ForYouViewModelTest` (90% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/foryou/impl/src/test/kotlin/com/google/samples/apps/nowinandroid/feature/foryou/impl/ForYouViewModelTest.kt:56:1`
- **Summary:** Type with excessive responsibilities, methods, or lines of code violating SRP.
- **Evidence Trail:**
  - `+90%` (SRP_MASSIVE_VIEWMODEL): Type 'ForYouViewModelTest' is a Massive ViewModel / God Class (434 lines, 13 methods, 19 properties) violating SRP

### 499. massive_viewmodel_srp on `SearchViewModelTest` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `class`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/search/impl/src/test/kotlin/com/google/samples/apps/nowinandroid/feature/search/impl/SearchViewModelTest.kt:50:1`
- **Summary:** Type with excessive responsibilities, methods, or lines of code violating SRP.
- **Evidence Trail:**
  - `+80%` (SRP_MASSIVE_VIEWMODEL): Type 'SearchViewModelTest' is a Massive ViewModel / God Class (131 lines, 10 methods, 15 properties) violating SRP

### 500. fat_interface_isp on `UserDataRepository` (85% [VERY_HIGH])
- **Category:** `principle`
- **Target Kind:** `interface`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/core/data/src/main/kotlin/com/google/samples/apps/nowinandroid/core/data/repository/UserDataRepository.kt:24:1`
- **Summary:** Interface declaring too many required methods, forcing implementors to depend on unused methods.
- **Evidence Trail:**
  - `+85%` (ISP_FAT_INTERFACE): Interface 'UserDataRepository' is a Fat Interface declaring 8 required methods; consider splitting into smaller role interfaces

### 501. dry_duplicate_logic on `TopicFtsDao.getCount` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** N/A
- **Summary:** Duplicated algorithmic sequences across multiple functions or classes.
- **Evidence Trail:**
  - `+80%` (DRY_DUPLICATE_CODE): Identical logic duplicated across 2 function(s): TopicFtsDao.getCount, NewsResourceFtsDao.getCount

### 502. dry_duplicate_logic on `FakeTopicsRepository.syncWith` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** N/A
- **Summary:** Duplicated algorithmic sequences across multiple functions or classes.
- **Evidence Trail:**
  - `+80%` (DRY_DUPLICATE_CODE): Identical logic duplicated across 4 function(s): FakeTopicsRepository.syncWith, FakeNewsRepository.syncWith, TestNewsRepository.syncWith

### 503. dry_duplicate_logic on `NiaAppScreenSizesScreenshotTests.setup` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** N/A
- **Summary:** Duplicated algorithmic sequences across multiple functions or classes.
- **Evidence Trail:**
  - `+80%` (DRY_DUPLICATE_CODE): Identical logic duplicated across 3 function(s): NiaAppScreenSizesScreenshotTests.setup, SnackbarScreenshotTests.setup, SnackbarInsetsScreenshotTests.setup

### 504. dry_duplicate_logic on `NiaAppScreenSizesScreenshotTests.setTimeZone` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** N/A
- **Summary:** Duplicated algorithmic sequences across multiple functions or classes.
- **Evidence Trail:**
  - `+80%` (DRY_DUPLICATE_CODE): Identical logic duplicated across 4 function(s): NiaAppScreenSizesScreenshotTests.setTimeZone, SnackbarScreenshotTests.setTimeZone, SnackbarInsetsScreenshotTests.setTimeZone

### 505. dry_duplicate_logic on `ScrollTopicListBenchmark.benchmarkStateChange` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** N/A
- **Summary:** Duplicated algorithmic sequences across multiple functions or classes.
- **Evidence Trail:**
  - `+80%` (DRY_DUPLICATE_CODE): Identical logic duplicated across 2 function(s): ScrollTopicListBenchmark.benchmarkStateChange, TopicsScreenRecompositionBenchmark.benchmarkStateChange

### 506. dry_duplicate_logic on `ForYouViewModel.setNewsResourceViewed` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** N/A
- **Summary:** Duplicated algorithmic sequences across multiple functions or classes.
- **Evidence Trail:**
  - `+80%` (DRY_DUPLICATE_CODE): Identical logic duplicated across 4 function(s): ForYouViewModel.setNewsResourceViewed, TopicViewModel.setNewsResourceViewed, SearchViewModel.setNewsResourceViewed

### 507. dry_duplicate_logic on `SearchViewModel.followTopic` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** N/A
- **Summary:** Duplicated algorithmic sequences across multiple functions or classes.
- **Evidence Trail:**
  - `+80%` (DRY_DUPLICATE_CODE): Identical logic duplicated across 2 function(s): SearchViewModel.followTopic, InterestsViewModel.followTopic

### 508. demeter_law_train_wreck on `apply` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/AndroidApplicationComposeConventionPlugin.kt:25:1`
- **Summary:** Deep navigation across indirect object graphs (`a.b.c.d.e`), increasing coupling.
- **Evidence Trail:**
  - `+80%` (DEMETER_LAW_TRAIN_WRECK): Function 'apply' violates Law of Demeter with deep navigation chain: 'org.jetbrains.kotlin.plugin.compose'

### 509. demeter_law_train_wreck on `apply` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/AndroidFeatureApiConventionPlugin.kt:23:1`
- **Summary:** Deep navigation across indirect object graphs (`a.b.c.d.e`), increasing coupling.
- **Evidence Trail:**
  - `+80%` (DEMETER_LAW_TRAIN_WRECK): Function 'apply' violates Law of Demeter with deep navigation chain: 'org.jetbrains.kotlin.plugin.serialization'

### 510. demeter_law_train_wreck on `apply` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/build-logic/convention/src/main/kotlin/AndroidLibraryComposeConventionPlugin.kt:25:1`
- **Summary:** Deep navigation across indirect object graphs (`a.b.c.d.e`), increasing coupling.
- **Evidence Trail:**
  - `+80%` (DEMETER_LAW_TRAIN_WRECK): Function 'apply' violates Law of Demeter with deep navigation chain: 'org.jetbrains.kotlin.plugin.compose'

### 511. demeter_law_train_wreck on `feed_whenRemovingBookmark_removesBookmark` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/feature/bookmarks/impl/src/androidTest/kotlin/com/google/samples/apps/nowinandroid/feature/bookmarks/impl/BookmarksScreenTest.kt:113:1`
- **Summary:** Deep navigation across indirect object graphs (`a.b.c.d.e`), increasing coupling.
- **Evidence Trail:**
  - `+80%` (DEMETER_LAW_TRAIN_WRECK): Function 'feed_whenRemovingBookmark_removesBookmark' violates Law of Demeter with deep navigation chain: 'com.google.samples.apps.nowinandroid'

### 512. demeter_law_train_wreck on `syncWorkNotification` (80% [HIGH])
- **Category:** `principle`
- **Target Kind:** `function`
- **Location:** `/Volumes/External/Code/DPX-Kotlin/benchmarks/nowinandroid/sync/work/src/main/kotlin/com/google/samples/apps/nowinandroid/sync/initializers/SyncWorkHelpers.kt:53:1`
- **Summary:** Deep navigation across indirect object graphs (`a.b.c.d.e`), increasing coupling.
- **Evidence Trail:**
  - `+80%` (DEMETER_LAW_TRAIN_WRECK): Function 'syncWorkNotification' violates Law of Demeter with deep navigation chain: 'com.google.samples.apps.nowinandroid'
