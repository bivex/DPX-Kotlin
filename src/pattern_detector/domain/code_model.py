"""Domain AST and structural model for Kotlin codebases."""

from __future__ import annotations

from dataclasses import dataclass, field
from pattern_detector.domain.value_objects import SourceLocation


@dataclass
class KotlinProperty:
    """Represents a property / field declaration in Kotlin."""

    name: str
    type_name: str = ""
    is_val: bool = True
    is_var: bool = False
    is_const: bool = False
    is_lazy: bool = False
    is_delegated: bool = False
    delegate_expression: str | None = None
    is_private: bool = False
    is_override: bool = False
    annotations: list[str] = field(default_factory=list)
    initializer: str | None = None
    location: SourceLocation | None = None
    raw_text: str = ""


@dataclass
class KotlinFunction:
    """Represents a function / method / constructor in Kotlin."""

    name: str
    receiver_type: str | None = None  # e.g. "String" in "fun String.clean()"
    parameters: list[tuple[str, str]] = field(default_factory=list)  # (name, type)
    return_type: str = "Unit"
    is_suspend: bool = False
    is_inline: bool = False
    is_operator: bool = False
    is_infix: bool = False
    is_private: bool = False
    is_override: bool = False
    annotations: list[str] = field(default_factory=list)
    body: str = ""
    branch_count: int = 1
    location: SourceLocation | None = None
    raw_text: str = ""

    @property
    def is_extension(self) -> bool:
        return self.receiver_type is not None


@dataclass
class KotlinType:
    """Represents a class, interface, object, enum, or sealed hierarchy in Kotlin."""

    name: str
    kind: str = "class"  # class, interface, object, enum, annotation, data_class, value_class, sealed_class, sealed_interface
    is_sealed: bool = False
    is_data: bool = False
    is_value: bool = False
    is_companion: bool = False
    is_object: bool = False
    inherited_types: list[str] = field(default_factory=list)
    annotations: list[str] = field(default_factory=list)
    generic_parameters: list[str] = field(default_factory=list)
    properties: list[KotlinProperty] = field(default_factory=list)
    functions: list[KotlinFunction] = field(default_factory=list)
    companion_objects: list[KotlinType] = field(default_factory=list)
    location: SourceLocation | None = None
    line_count: int = 1
    raw_text: str = ""


@dataclass
class KotlinFile:
    """Represents a single parsed Kotlin file (.kt or .kts)."""

    file_path: str
    package_name: str = ""
    imports: list[str] = field(default_factory=list)
    types: list[KotlinType] = field(default_factory=list)
    global_functions: list[KotlinFunction] = field(default_factory=list)
    global_properties: list[KotlinProperty] = field(default_factory=list)
    lines: list[str] = field(default_factory=list)
    raw_content: str = ""


@dataclass
class CodeModel:
    """Aggregate model representing all parsed Kotlin files in the target codebase."""

    files: list[KotlinFile] = field(default_factory=list)
    target_path: str = ""

    @property
    def all_types(self) -> list[KotlinType]:
        types: list[KotlinType] = []
        for f in self.files:
            types.extend(f.types)
            for t in f.types:
                types.extend(t.companion_objects)
        return types

    @property
    def classes(self) -> list[KotlinType]:
        return [t for t in self.all_types if t.kind in ("class", "data_class", "value_class", "sealed_class")]

    @property
    def interfaces(self) -> list[KotlinType]:
        return [t for t in self.all_types if t.kind in ("interface", "sealed_interface")]

    @property
    def objects(self) -> list[KotlinType]:
        return [t for t in self.all_types if t.is_object or t.kind == "object"]

    @property
    def sealed_types(self) -> list[KotlinType]:
        return [t for t in self.all_types if t.is_sealed or "sealed" in t.kind]

    @property
    def all_functions(self) -> list[KotlinFunction]:
        fns: list[KotlinFunction] = []
        for f in self.files:
            fns.extend(f.global_functions)
            for t in f.types:
                fns.extend(t.functions)
                for comp in t.companion_objects:
                    fns.extend(comp.functions)
        return fns

    @property
    def all_properties(self) -> list[KotlinProperty]:
        props: list[KotlinProperty] = []
        for f in self.files:
            props.extend(f.global_properties)
            for t in f.types:
                props.extend(t.properties)
                for comp in t.companion_objects:
                    props.extend(comp.properties)
        return props

    @property
    def extensions(self) -> list[KotlinFunction]:
        return [fn for fn in self.all_functions if fn.is_extension]
