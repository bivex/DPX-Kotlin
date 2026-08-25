"""Rules registry and aggregation factory for Kotlin pattern detector."""

from __future__ import annotations

from pattern_detector.domain.rules.base import BaseRule
from pattern_detector.domain.rules.idiomatic_rules import (
    CompanionStaticFactoryRule,
    DelegatedPropertyLazyRule,
    ExtensionFunctionAdapterRule,
    InlineValueClassRule,
    OperatorOverloadingDslRule,
    ScopeFunctionChainRule,
    SealedHierarchyAdtRule,
)
from pattern_detector.domain.rules.coroutines_rules import (
    ChannelActorConcurrencyRule,
    DispatcherIoOffloadRule,
    StateFlowReactiveStreamRule,
    StructuredConcurrencyScopeRule,
    SuspendingFunctionAsyncRule,
)
from pattern_detector.domain.rules.compose_dsl_rules import (
    ComposeDeclarativeViewRule,
    RememberMutableStateRule,
    TypeSafeBuilderDslRule,
    ViewModelStateHolderRule,
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
from pattern_detector.domain.rules.resilience_safety_rules import (
    ForceCastHazardRule,
    ForceNullAssertionHazardRule,
    GlobalScopeCoroutineLeakRule,
    MainThreadBlockingCallRule,
    NonCancellationExceptionSwallowRule,
    StrongContextLeakRule,
)
from pattern_detector.domain.rules.solid_principles_rules import (
    DemeterLawTrainWreckRule,
    DryDuplicateLogicRule,
    DynamicCastWhenCascadeOcpRule,
    FatInterfaceIspRule,
    KissCyclomaticComplexityRule,
    KissLongParameterListRule,
    MassiveViewModelSrpRule,
)

DEFAULT_RULES: list[type[BaseRule]] = [
    # 1. Kotlin Idiomatic
    ExtensionFunctionAdapterRule,
    DelegatedPropertyLazyRule,
    SealedHierarchyAdtRule,
    InlineValueClassRule,
    CompanionStaticFactoryRule,
    OperatorOverloadingDslRule,
    ScopeFunctionChainRule,

    # 2. Coroutines & Concurrency
    StructuredConcurrencyScopeRule,
    StateFlowReactiveStreamRule,
    ChannelActorConcurrencyRule,
    SuspendingFunctionAsyncRule,
    DispatcherIoOffloadRule,

    # 3. Compose & DSL
    TypeSafeBuilderDslRule,
    ComposeDeclarativeViewRule,
    RememberMutableStateRule,
    ViewModelStateHolderRule,

    # 4. GoF Creational (5/5)
    SingletonObjectDeclarationRule,
    FactoryMethodRule,
    AbstractFactoryRule,
    BuilderFluentChainRule,
    PrototypeDataCopyRule,

    # 5. GoF Structural (7/7)
    AdapterInterfaceDelegationRule,
    BridgeImplementorRule,
    CompositeViewTreeRule,
    DecoratorByDelegationRule,
    FacadeCoordinatorRule,
    FlyweightPoolCacheRule,
    ProxyVirtualOrRemoteRule,

    # 6. GoF Behavioral (11/11)
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

    # 7. Resilience & Hazards
    GlobalScopeCoroutineLeakRule,
    NonCancellationExceptionSwallowRule,
    ForceNullAssertionHazardRule,
    ForceCastHazardRule,
    MainThreadBlockingCallRule,
    StrongContextLeakRule,

    # 8. SOLID & Quality
    MassiveViewModelSrpRule,
    FatInterfaceIspRule,
    DynamicCastWhenCascadeOcpRule,
    KissCyclomaticComplexityRule,
    KissLongParameterListRule,
    DryDuplicateLogicRule,
    DemeterLawTrainWreckRule,
]


def get_default_rules() -> list[BaseRule]:
    """Instantiate and return the full suite of default Kotlin rules."""
    return [
        # 1. Idiomatic
        ExtensionFunctionAdapterRule(),
        DelegatedPropertyLazyRule(),
        SealedHierarchyAdtRule(),
        InlineValueClassRule(),
        CompanionStaticFactoryRule(),
        OperatorOverloadingDslRule(),
        ScopeFunctionChainRule(),

        # 2. Coroutines
        StructuredConcurrencyScopeRule(),
        StateFlowReactiveStreamRule(),
        ChannelActorConcurrencyRule(),
        SuspendingFunctionAsyncRule(),
        DispatcherIoOffloadRule(),

        # 3. Compose & DSL
        TypeSafeBuilderDslRule(),
        ComposeDeclarativeViewRule(),
        RememberMutableStateRule(),
        ViewModelStateHolderRule(),

        # 4. Creational (GoF 5/5)
        SingletonObjectDeclarationRule(),
        FactoryMethodRule(),
        AbstractFactoryRule(),
        BuilderFluentChainRule(),
        PrototypeDataCopyRule(),

        # 5. Structural (GoF 7/7)
        AdapterInterfaceDelegationRule(),
        BridgeImplementorRule(),
        CompositeViewTreeRule(),
        DecoratorByDelegationRule(),
        FacadeCoordinatorRule(),
        FlyweightPoolCacheRule(),
        ProxyVirtualOrRemoteRule(),

        # 6. Behavioral (GoF 11/11)
        ChainOfResponsibilityRule(),
        CommandActionObjectRule(),
        InterpreterExpressionAstRule(),
        IteratorSequenceFlowRule(),
        MediatorCoordinatorRule(),
        MementoSerializableStateRule(),
        ObserverFlowPublishedRule(),
        StateSealedClassFsmRule(),
        StrategyLambdaInjectionRule(),
        TemplateMethodAlgorithmRule(),
        VisitorSealedWhenRule(),

        # 7. Resilience & Hazards
        GlobalScopeCoroutineLeakRule(),
        NonCancellationExceptionSwallowRule(),
        ForceNullAssertionHazardRule(),
        ForceCastHazardRule(),
        MainThreadBlockingCallRule(),
        StrongContextLeakRule(),

        # 8. SOLID & Quality
        MassiveViewModelSrpRule(),
        FatInterfaceIspRule(),
        DynamicCastWhenCascadeOcpRule(),
        KissCyclomaticComplexityRule(),
        KissLongParameterListRule(),
        DryDuplicateLogicRule(),
        DemeterLawTrainWreckRule(),
    ]
