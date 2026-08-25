"""Unit tests for Kotlin Coroutines and Concurrency detection rules."""

from __future__ import annotations

from pattern_detector.adapters.outbound.parsers.native_kotlin_parser import NativeKotlinParserAdapter
from pattern_detector.domain.rules.coroutines_rules import (
    ChannelActorConcurrencyRule,
    DispatcherIoOffloadRule,
    StateFlowReactiveStreamRule,
    StructuredConcurrencyScopeRule,
    SuspendingFunctionAsyncRule,
)
from pattern_detector.domain.value_objects import PatternType


def test_structured_concurrency_scope() -> None:
    code = """
    package com.example.service

    class BatchProcessor(private val scope: CoroutineScope) {
        fun start() {
            scope.launch {
                coroutineScope {
                    launch { doWork1() }
                    launch { doWork2() }
                }
            }
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("BatchProcessor.kt", code)])

    rule = StructuredConcurrencyScopeRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.STRUCTURED_CONCURRENCY_SCOPE
    assert detections[0].target_name == "BatchProcessor"


def test_stateflow_reactive_stream() -> None:
    code = """
    package com.example.viewmodel

    class UserViewModel {
        private val _userState = MutableStateFlow<UserState>(UserState.Empty)
        val userState: StateFlow<UserState> = _userState.asStateFlow()
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("UserViewModel.kt", code)])

    rule = StateFlowReactiveStreamRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.STATEFLOW_REACTIVE_STREAM
    assert detections[0].target_name == "UserViewModel"


def test_channel_actor_concurrency() -> None:
    code = """
    package com.example.queue

    class WorkQueueManager {
        private val taskChannel = Channel<Task>(Channel.BUFFERED)
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("WorkQueueManager.kt", code)])

    rule = ChannelActorConcurrencyRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.CHANNEL_ACTOR_CONCURRENCY


def test_suspending_function_async() -> None:
    code = """
    package com.example.repo

    suspend fun fetchAccountDetails(id: String): AccountDetails {
        return api.getAccount(id)
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("AccountRepo.kt", code)])

    rule = SuspendingFunctionAsyncRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.SUSPENDING_FUNCTION_ASYNC
    assert detections[0].target_name == "fetchAccountDetails"


def test_dispatcher_io_offload() -> None:
    code = """
    package com.example.data

    suspend fun readDatabaseFile(): ByteArray {
        return withContext(Dispatchers.IO) {
            File("data.db").readBytes()
        }
    }
    """
    parser = NativeKotlinParserAdapter()
    model = parser.parse_codebase([("DbReader.kt", code)])

    rule = DispatcherIoOffloadRule()
    detections = rule.evaluate(model)

    assert len(detections) == 1
    assert detections[0].pattern_type == PatternType.DISPATCHER_IO_OFFLOAD
