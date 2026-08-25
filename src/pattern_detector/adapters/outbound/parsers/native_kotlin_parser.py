"""High-speed native parser adapter for Kotlin source code (.kt / .kts)."""

from __future__ import annotations

import re
from pattern_detector.domain.code_model import (
    CodeModel,
    KotlinFile,
    KotlinFunction,
    KotlinProperty,
    KotlinType,
)
from pattern_detector.domain.value_objects import SourceLocation
from pattern_detector.ports.outbound import ParserPort


class NativeKotlinParserAdapter(ParserPort):
    """Linear, robust single-pass parser extracting Kotlin AST declaration semantics."""

    PACKAGE_PATTERN = re.compile(r"^\s*package\s+([A-Za-z0-9_.]+)")
    IMPORT_PATTERN = re.compile(r"^\s*import\s+([A-Za-z0-9_.*]+)")

    TYPE_HEADER_PATTERN = re.compile(
        r"^(?P<attrs>(?:@\w+(?:\([^)]*\))?\s+)*)"
        r"(?P<modifiers>(?:public|private|protected|internal|open|final|abstract|sealed|data|inline|value|enum)\s+)*"
        r"(?P<kind>class|interface|object|enum\s+class|data\s+class|value\s+class|sealed\s+class|sealed\s+interface|companion\s+object)\s*"
        r"(?P<name>[A-Za-z0-9_]+)?"
        r"(?:<(?P<generics>[^>]+)>)?"
        r"(?:\s*\((?P<constructor_params>[^)]*)\))?"
        r"(?:\s*:\s*(?P<inherits>[^{]+))?"
    )

    FUNCTION_HEADER_PATTERN = re.compile(
        r"^(?P<attrs>(?:@\w+(?:\([^)]*\))?\s+)*)"
        r"(?P<modifiers>(?:public|private|protected|internal|open|final|abstract|override|suspend|inline|operator|infix|tailrec)\s+)*"
        r"fun\s+"
        r"(?:<(?P<generics>[^>]+)>\s*)?"
        r"(?:(?P<receiver>[A-Za-z0-9_<>?]+)\.)?"
        r"(?P<name>[A-Za-z0-9_]+)\s*"
        r"\((?P<params>[^)]*)\)"
        r"(?:\s*:\s*(?P<return_type>[^{=\n]+))?"
    )

    PROPERTY_PATTERN = re.compile(
        r"^(?P<attrs>(?:@\w+(?:\([^)]*\))?\s+)*)"
        r"(?P<modifiers>(?:public|private|protected|internal|open|final|abstract|override|const|lateinit)\s+)*"
        r"(?P<mutability>val|var)\s+"
        r"(?P<name>[A-Za-z0-9_]+)"
        r"(?:\s*:\s*(?P<type_name>[^=;{\n]+?))?"
        r"(?:\s+by\s+(?P<delegate>[^;{\n]+)|\s*=\s*(?P<init>[^;{\n]+))?"
        r"\s*$"
    )

    BRANCH_KEYWORDS = re.compile(r"\b(if\s*\(|when\s*\(|when\s*\{|for\s*\(|while\s*\(|catch\s*\(|&&|\|\||\?:)")

    def parse_file(self, file_path: str, content: str) -> KotlinFile:
        lines = content.splitlines()
        file_obj = KotlinFile(file_path=file_path, raw_content=content, lines=lines)

        current_type: KotlinType | None = None
        current_companion: KotlinType | None = None
        brace_depth = 0
        type_brace_depth = 0
        companion_brace_depth = 0
        method_brace_depth = 0
        current_method: KotlinFunction | None = None
        current_method_body: list[str] = []
        pending_attributes: list[str] = []

        for line_idx, raw_line in enumerate(lines, 1):
            trimmed = raw_line.strip()

            # Skip comments
            if trimmed.startswith("//") or trimmed.startswith("/*") or trimmed.startswith("*"):
                continue

            # Check Package
            pkg_m = self.PACKAGE_PATTERN.match(trimmed)
            if pkg_m:
                file_obj.package_name = pkg_m.group(1)
                continue

            # Check Import
            imp_m = self.IMPORT_PATTERN.match(trimmed)
            if imp_m:
                file_obj.imports.append(imp_m.group(1))
                continue

            # Capture standalone annotation
            if trimmed.startswith("@") and not any(kw in trimmed for kw in ("class", "interface", "object", "fun", "val", "var")):
                pending_attributes.append(trimmed)
                continue

            # Check Type Header
            type_match = self.TYPE_HEADER_PATTERN.match(trimmed)
            if type_match and (brace_depth == 0 or (current_type and "companion" in type_match.group("kind"))):
                raw_kind = type_match.group("kind")
                name = type_match.group("name") or ("Companion" if "companion" in raw_kind else "Anonymous")
                mods = type_match.group("modifiers") or ""
                inherits_str = type_match.group("inherits") or ""
                attrs_str = type_match.group("attrs") or ""
                generics_str = type_match.group("generics") or ""
                ctor_params_str = type_match.group("constructor_params") or ""

                all_attrs = pending_attributes + [a.strip() for a in attrs_str.split() if a.startswith("@")]
                pending_attributes = []

                inherits = [inh.strip() for inh in inherits_str.split(",") if inh.strip()]
                generics = [g.strip() for g in generics_str.split(",") if g.strip()]

                is_companion = "companion" in raw_kind
                is_sealed = "sealed" in raw_kind or "sealed" in mods
                is_data = "data" in raw_kind or "data" in mods
                is_value = "value" in raw_kind or "value" in mods
                is_object = "object" in raw_kind

                normalized_kind = "class"
                if "interface" in raw_kind:
                    normalized_kind = "sealed_interface" if is_sealed else "interface"
                elif is_sealed:
                    normalized_kind = "sealed_class"
                elif is_data:
                    normalized_kind = "data_class"
                elif is_value:
                    normalized_kind = "value_class"
                elif is_object:
                    normalized_kind = "companion_object" if is_companion else "object"

                new_type = KotlinType(
                    name=name,
                    kind=normalized_kind,
                    is_sealed=is_sealed,
                    is_data=is_data,
                    is_value=is_value,
                    is_companion=is_companion,
                    is_object=is_object,
                    inherited_types=inherits,
                    annotations=all_attrs,
                    generic_parameters=generics,
                    location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                    raw_text=raw_line,
                )

                # Parse primary constructor properties if data class
                if ctor_params_str and (is_data or is_value or "class" in normalized_kind):
                    for param in ctor_params_str.split(","):
                        p_clean = param.strip()
                        if "val " in p_clean or "var " in p_clean:
                            p_is_val = "val " in p_clean
                            p_body = p_clean.replace("val ", "").replace("var ", "").replace("override ", "").strip()
                            if ":" in p_body:
                                p_name, p_type = p_body.split(":", 1)
                                new_type.properties.append(
                                    KotlinProperty(
                                        name=p_name.strip(),
                                        type_name=p_type.strip(),
                                        is_val=p_is_val,
                                        is_var=not p_is_val,
                                        location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                                        raw_text=p_clean,
                                    )
                                )

                if is_companion and current_type:
                    current_companion = new_type
                    companion_brace_depth = brace_depth
                    current_type.companion_objects.append(new_type)
                else:
                    current_type = new_type
                    type_brace_depth = brace_depth
                    file_obj.types.append(new_type)

            # Check Property
            prop_match = self.PROPERTY_PATTERN.match(trimmed)
            if prop_match and not trimmed.startswith("fun "):
                p_name = prop_match.group("name")
                p_mut = prop_match.group("mutability")
                p_type = (prop_match.group("type_name") or "").strip()
                p_delegate = (prop_match.group("delegate") or "").strip()
                p_init = (prop_match.group("init") or "").strip()
                p_mods = prop_match.group("modifiers") or ""
                p_attrs_str = prop_match.group("attrs") or ""

                all_p_attrs = pending_attributes + [a.strip() for a in p_attrs_str.split() if a.startswith("@")]
                pending_attributes = []

                prop = KotlinProperty(
                    name=p_name,
                    type_name=p_type,
                    is_val=(p_mut == "val"),
                    is_var=(p_mut == "var"),
                    is_const=("const" in p_mods),
                    is_lazy=("lazy" in p_delegate or "lazy" in p_init),
                    is_delegated=bool(p_delegate),
                    delegate_expression=p_delegate or None,
                    is_private=("private" in p_mods),
                    is_override=("override" in p_mods),
                    annotations=all_p_attrs,
                    initializer=p_init or None,
                    location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                    raw_text=raw_line,
                )

                if current_companion:
                    current_companion.properties.append(prop)
                elif current_type:
                    current_type.properties.append(prop)
                else:
                    file_obj.global_properties.append(prop)

            # Check Function Header
            fn_match = self.FUNCTION_HEADER_PATTERN.match(trimmed)
            if fn_match:
                f_name = fn_match.group("name")
                f_receiver = fn_match.group("receiver")
                f_params_str = fn_match.group("params") or ""
                f_ret = (fn_match.group("return_type") or "Unit").strip()
                f_mods = fn_match.group("modifiers") or ""
                f_attrs_str = fn_match.group("attrs") or ""

                all_f_attrs = pending_attributes + [a.strip() for a in f_attrs_str.split() if a.startswith("@")]
                pending_attributes = []

                params: list[tuple[str, str]] = []
                for p in f_params_str.split(","):
                    p_clean = p.strip()
                    if ":" in p_clean:
                        p_n, p_t = p_clean.split(":", 1)
                        params.append((p_n.strip(), p_t.strip()))
                    elif p_clean:
                        params.append((p_clean, "Any"))

                current_method = KotlinFunction(
                    name=f_name,
                    receiver_type=f_receiver,
                    parameters=params,
                    return_type=f_ret,
                    is_suspend=("suspend" in f_mods),
                    is_inline=("inline" in f_mods),
                    is_operator=("operator" in f_mods),
                    is_infix=("infix" in f_mods),
                    is_private=("private" in f_mods),
                    is_override=("override" in f_mods),
                    annotations=all_f_attrs,
                    location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                    raw_text=raw_line,
                )
                current_method_body = [raw_line]
                method_brace_depth = brace_depth

                if current_companion:
                    current_companion.functions.append(current_method)
                elif current_type:
                    current_type.functions.append(current_method)
                else:
                    file_obj.global_functions.append(current_method)

            # Accumulate method body
            if current_method:
                current_method_body.append(raw_line)
                branches = len(self.BRANCH_KEYWORDS.findall(raw_line))
                current_method.branch_count += branches

            # Track brace depth
            open_braces = raw_line.count("{")
            close_braces = raw_line.count("}")
            brace_depth += open_braces - close_braces

            if current_method and brace_depth <= method_brace_depth and close_braces > 0:
                current_method.body = "\n".join(current_method_body)
                current_method = None
                current_method_body = []

            if current_companion and brace_depth <= companion_brace_depth and close_braces > 0:
                current_companion = None

            if current_type and brace_depth <= type_brace_depth and close_braces > 0:
                if current_type.location:
                    current_type.line_count = line_idx - current_type.location.line + 1
                current_type = None

        return file_obj

    def parse_codebase(self, files: list[tuple[str, str]], target_path: str = "") -> CodeModel:
        model = CodeModel(target_path=target_path)
        for fpath, content in files:
            kt_file = self.parse_file(fpath, content)
            model.files.append(kt_file)
        return model
