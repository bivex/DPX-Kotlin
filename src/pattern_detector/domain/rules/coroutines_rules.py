"""Kotlin Coroutines, Flow, and Structured Concurrency rules."""

from __future__ import annotations

import re
from pattern_detector.domain.code_model import CodeModel
from pattern_detector.domain.detection import Detection
from pattern_detector.domain.rules.base import BaseRule
from pattern_detector.domain.value_objects import (
    Confidence,
    Evidence,
    PatternCategory,
    PatternType,
)


class StructuredConcurrencyScopeRule(BaseRule):
    """Detects structured concurrency lifecycle scopes (`CoroutineScope`, `coroutineScope`, `supervisorScope`, `viewModelScope`)."""

    SCOPE_PATTERN = re.compile(r"\b(coroutineScope|supervisorScope|viewModelScope|lifecycleScope|CoroutineScope)\b")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_types:
            has_scope = any(self.SCOPE_PATTERN.search(p.raw_text or "") for p in t.properties) or any(self.SCOPE_PATTERN.search(fn.body or "") for fn in t.functions)
            if has_scope or "CoroutineScope" in t.inherited_types:
                evidences = [
                    Evidence(
                        rule_code="COROUTINES_STRUCTURED_SCOPE",
                        description=f"Type '{t.name}' bounds asynchronous jobs within structured CoroutineScope",
                        weight=0.90,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.STRUCTURED_CONCURRENCY_SCOPE,
                        pattern_category=PatternCategory.COROUTINES_CONCURRENCY,
                        target_name=t.name,
                        target_kind=t.kind,
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class StateFlowReactiveStreamRule(BaseRule):
    """Detects `StateFlow` / `SharedFlow` reactive state streams."""

    FLOW_PATTERN = re.compile(r"\b(MutableStateFlow|StateFlow|MutableSharedFlow|SharedFlow)\s*<")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_types:
            flow_props = [
                p for p in t.properties
                if self.FLOW_PATTERN.search(p.type_name) or self.FLOW_PATTERN.search(p.raw_text or "")
            ]
            if flow_props:
                evidences = [
                    Evidence(
                        rule_code="COROUTINES_STATEFLOW_STREAM",
                        description=f"Type '{t.name}' defines {len(flow_props)} hot StateFlow/SharedFlow reactive stream(s) ({', '.join(p.name for p in flow_props[:2])})",
                        weight=0.95,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.STATEFLOW_REACTIVE_STREAM,
                        pattern_category=PatternCategory.COROUTINES_CONCURRENCY,
                        target_name=t.name,
                        target_kind=t.kind,
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class ChannelActorConcurrencyRule(BaseRule):
    """Detects `Channel<T>` and actor concurrency models."""

    CHANNEL_PATTERN = re.compile(r"\b(Channel|SendChannel|ReceiveChannel)\s*<|\bactor\s*<")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_types:
            channel_props = [
                p for p in t.properties
                if self.CHANNEL_PATTERN.search(p.type_name) or self.CHANNEL_PATTERN.search(p.raw_text or "")
            ]
            if channel_props:
                evidences = [
                    Evidence(
                        rule_code="COROUTINES_CHANNEL_ACTOR",
                        description=f"Type '{t.name}' coordinates concurrent communication via CSP Channel(s)",
                        weight=0.90,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.CHANNEL_ACTOR_CONCURRENCY,
                        pattern_category=PatternCategory.COROUTINES_CONCURRENCY,
                        target_name=t.name,
                        target_kind=t.kind,
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class SuspendingFunctionAsyncRule(BaseRule):
    """Detects non-blocking `suspend fun` asynchronous execution."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if fn.is_suspend:
                evidences = [
                    Evidence(
                        rule_code="COROUTINES_SUSPEND_FUNCTION",
                        description=f"Suspending function '{fn.name}' enables non-blocking asynchronous continuation",
                        weight=0.85,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.SUSPENDING_FUNCTION_ASYNC,
                        pattern_category=PatternCategory.COROUTINES_CONCURRENCY,
                        target_name=fn.name,
                        target_kind="suspend_function",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections


class DispatcherIoOffloadRule(BaseRule):
    """Detects explicit thread-affinity offloading (`withContext(Dispatchers.IO)`)."""

    DISPATCHER_PATTERN = re.compile(r"\bwithContext\s*\(\s*Dispatchers\.(IO|Default)\s*\)")

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for fn in model.all_functions:
            if self.DISPATCHER_PATTERN.search(fn.body or ""):
                evidences = [
                    Evidence(
                        rule_code="COROUTINES_DISPATCHER_OFFLOAD",
                        description=f"Function '{fn.name}' explicitly offloads blocking computation using withContext(Dispatchers)",
                        weight=0.90,
                        location=fn.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.DISPATCHER_IO_OFFLOAD,
                        pattern_category=PatternCategory.COROUTINES_CONCURRENCY,
                        target_name=fn.name,
                        target_kind="function",
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=fn.location,
                        evidences=evidences,
                    )
                )
        return detections
