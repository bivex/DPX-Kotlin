"""GoF Behavioral design pattern detection rules for Kotlin (11/11)."""

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


class ChainOfResponsibilityRule(BaseRule):
    """Detects Chain of Responsibility pattern holding `next` handler pointer or interceptor pipeline."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            has_next = any(
                p.name in ("next", "nextHandler", "successor") or p.type_name in (t.name, f"{t.name}?") or "Handler" in p.type_name
                for p in t.properties
            )
            if (has_next and "Handler" in t.name) or "Interceptor" in t.name or "Chain" in t.name:
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_CHAIN_OF_RESPONSIBILITY",
                        description=f"Class '{t.name}' implements Chain of Responsibility delegating unhandled requests along handler chain",
                        weight=0.85,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.CHAIN_OF_RESPONSIBILITY,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=t.name,
                        target_kind="class",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class CommandActionObjectRule(BaseRule):
    """Detects Command pattern encapsulating operations into executable command/action objects."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_types:
            has_execute = any(fn.name in ("execute", "run", "perform", "undo", "invoke") for fn in t.functions)
            if ("Command" in t.name or "Action" in t.name) and (has_execute or "Command" in t.name):
                score = 0.90 if has_execute else 0.80
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_COMMAND_ACTION",
                        description=f"Type '{t.name}' encapsulates executable operation as a Command object",
                        weight=score,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.COMMAND_ACTION_OBJECT,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=t.name,
                        target_kind=t.kind,
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class InterpreterExpressionAstRule(BaseRule):
    """Detects Interpreter pattern evaluating expression trees via `interpret(context)` / `eval()`."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_types:
            has_interpret = any(fn.name in ("interpret", "evaluate", "eval") for fn in t.functions)
            if "Expression" in t.name or "AST" in t.name or (has_interpret and "Context" in t.raw_text):
                score = 0.90 if has_interpret else 0.80
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_INTERPRETER_EXPRESSION",
                        description=f"Type '{t.name}' implements Interpreter pattern evaluating domain expression AST",
                        weight=score,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.INTERPRETER_EXPRESSION_AST,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=t.name,
                        target_kind=t.kind,
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class IteratorSequenceFlowRule(BaseRule):
    """Detects Iterator / Sequence / Flow traversal."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_types:
            has_iterator = any(any(k in inh for k in ("Iterator", "Sequence", "Iterable", "Flow")) for inh in t.inherited_types)
            has_next = any(fn.name in ("next", "hasNext") for fn in t.functions)
            if has_iterator or has_next:
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_ITERATOR_SEQUENCE",
                        description=f"Type '{t.name}' conforms to Iterator / Sequence for lazy sequential element traversal",
                        weight=0.90,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.ITERATOR_SEQUENCE_FLOW,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=t.name,
                        target_kind=t.kind,
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class MediatorCoordinatorRule(BaseRule):
    """Detects Mediator / Coordinator pattern managing navigation and component communication flows."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            if "Coordinator" in t.name or "Mediator" in t.name or "Navigator" in t.name:
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_MEDIATOR_COORDINATOR",
                        description=f"Class '{t.name}' acts as Mediator / Coordinator decoupling components and managing navigation flows",
                        weight=0.85,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.MEDIATOR_COORDINATOR,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=t.name,
                        target_kind="class",
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class MementoSerializableStateRule(BaseRule):
    """Detects Memento pattern via `@Serializable` / `Parcelable` state snapshot."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_types:
            has_serializable = any("@Serializable" in a for a in t.annotations) or "Parcelable" in t.inherited_types or "Serializable" in t.inherited_types
            if "Snapshot" in t.name or "Memento" in t.name or (has_serializable and any(fn.name in ("createSnapshot", "restoreState", "saveState") for fn in t.functions)):
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_MEMENTO_SNAPSHOT",
                        description=f"Type '{t.name}' captures and externalizes object state as a Memento Snapshot",
                        weight=0.85,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.MEMENTO_SERIALIZABLE_STATE,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=t.name,
                        target_kind=t.kind,
                        confidence=Confidence(score=0.85, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class ObserverFlowPublishedRule(BaseRule):
    """Detects Observer pattern using Kotlin Coroutines `Flow`, `LiveData`, or Subject subscribers."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_types:
            flow_props = [
                p for p in t.properties
                if any(k in p.type_name for k in ("Flow", "LiveData", "Observable", "Subject"))
            ]
            if flow_props:
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_OBSERVER_FLOW",
                        description=f"Type '{t.name}' acts as Reactive Observer Subject publishing {len(flow_props)} stream(s)",
                        weight=0.90,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.OBSERVER_FLOW_PUBLISHED,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=t.name,
                        target_kind=t.kind,
                        confidence=Confidence(score=0.90, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class StateSealedClassFsmRule(BaseRule):
    """Detects State pattern modeled via Sealed Class / Interface hierarchies with state payloads."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.sealed_types:
            if "State" in t.name or "Status" in t.name or "Phase" in t.name or "UiState" in t.name:
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_STATE_SEALED_FSM",
                        description=f"Sealed type '{t.name}' models type-safe Finite State Machine (FSM) with associated lifecycle states",
                        weight=0.95,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.STATE_SEALED_CLASS_FSM,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=t.name,
                        target_kind=t.kind,
                        confidence=Confidence(score=0.95, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class StrategyLambdaInjectionRule(BaseRule):
    """Detects Strategy pattern via functional interface or lambda injection."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            strategy_props = [
                p for p in t.properties
                if "Strategy" in p.type_name or "Strategy" in p.name or "Formatter" in p.type_name or "Validator" in p.type_name
            ]
            if strategy_props or "Strategy" in t.name:
                score = 0.90 if "Strategy" in t.name else 0.80
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_STRATEGY_INJECTION",
                        description=f"Class '{t.name}' injects interchangeable Strategy algorithm via '{strategy_props[0].name if strategy_props else 'strategy'}'",
                        weight=score,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.STRATEGY_LAMBDA_INJECTION,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=t.name,
                        target_kind="class",
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class TemplateMethodAlgorithmRule(BaseRule):
    """Detects Template Method pattern defining algorithm skeleton with deferred step hooks."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.classes:
            has_template_methods = any(
                fn.name.startswith("process") or fn.name.startswith("execute") or fn.name.startswith("handle")
                for fn in t.functions
            )
            has_step_hooks = any(
                fn.name.startswith("step") or fn.name.startswith("before") or fn.name.startswith("after") or fn.name.startswith("on")
                for fn in t.functions
            )
            if (has_template_methods and has_step_hooks) or "Template" in t.name:
                score = 0.85
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_TEMPLATE_METHOD",
                        description=f"Class '{t.name}' implements Template Method algorithm skeleton coordinating lifecycle step hooks",
                        weight=score,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.TEMPLATE_METHOD_ALGORITHM,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=t.name,
                        target_kind="class",
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections


class VisitorSealedWhenRule(BaseRule):
    """Detects Visitor pattern via `accept(visitor)` or exhaustive `when` dispatch over sealed types."""

    def evaluate(self, model: CodeModel) -> list[Detection]:
        detections: list[Detection] = []
        for t in model.all_types:
            has_accept = any(fn.name == "accept" and any("visitor" in p[0].lower() or "Visitor" in p[1] for p in fn.parameters) for fn in t.functions)
            if has_accept or "Visitor" in t.name:
                score = 0.90 if has_accept else 0.80
                evidences = [
                    Evidence(
                        rule_code="BEHAVIORAL_VISITOR_PATTERN",
                        description=f"Type '{t.name}' implements Visitor pattern enabling double dispatch operations",
                        weight=score,
                        location=t.location,
                    )
                ]
                detections.append(
                    Detection(
                        pattern_type=PatternType.VISITOR_SEALED_WHEN,
                        pattern_category=PatternCategory.BEHAVIORAL,
                        target_name=t.name,
                        target_kind=t.kind,
                        confidence=Confidence(score=score, evidences=evidences),
                        primary_location=t.location,
                        evidences=evidences,
                    )
                )
        return detections
