"""Local runner for examples copied in LeetCode problem docstrings."""

from __future__ import annotations

import argparse
import ast
import copy
import inspect
import math
import sys
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import Any


class LeetCodeLocalJudgeError(Exception):
    """Base error for local LeetCode example judging."""


class LeetCodeParseError(LeetCodeLocalJudgeError):
    """Raised when a copied LeetCode example cannot be parsed."""


@dataclass(frozen=True)
class ExampleCase:
    index: int
    inputs: dict[str, Any]
    expected: Any


@dataclass(frozen=True)
class ExampleResult:
    case: ExampleCase
    actual: Any = None
    passed: bool = False
    error: BaseException | None = None


_EXAMPLE_HEADER = "Example "
_SECTION_LABELS = ("Input:", "Output:", "Explanation:", "Constraints:", "Example ")
_NAME_LITERALS = {
    "true": True,
    "false": False,
    "null": None,
}


def parse_examples(doc: str | None) -> list[ExampleCase]:
    if not doc:
        return []

    examples = []
    for index, block in enumerate(_example_blocks(doc), start=1):
        input_text = _read_section(block, "Input:")
        output_text = _read_section(block, "Output:")
        if input_text is None or output_text is None:
            continue
        examples.append(
            ExampleCase(
                index=index,
                inputs=parse_input(input_text),
                expected=parse_value(output_text),
            )
        )
    return examples


def parse_input(text: str) -> dict[str, Any]:
    expression = _parse_expression(f"_({text})")
    call = expression.body
    if not isinstance(call, ast.Call):
        raise LeetCodeParseError(f"Expected LeetCode input assignments, got: {text!r}")

    if call.args:
        raise LeetCodeParseError(f"Expected named input assignments, got: {text!r}")

    inputs = {}
    for keyword in call.keywords:
        if keyword.arg is None:
            raise LeetCodeParseError(f"Unsupported expanded input assignment: {text!r}")
        inputs[keyword.arg] = _literal_eval(keyword.value)
    return inputs


def parse_value(text: str) -> Any:
    expression = _parse_expression(text)
    return _literal_eval(expression.body)


def run_examples(
    solution_cls: type,
    doc: str | None = None,
    *,
    method_name: str | None = None,
    tolerance: float = 1e-5,
) -> list[ExampleResult]:
    cases = parse_examples(doc or _doc_for(solution_cls))
    if not cases:
        raise LeetCodeParseError("No LeetCode examples found in the supplied docstring.")

    method_name = method_name or _solution_method_name(solution_cls)
    results = []
    for case in cases:
        before = copy.deepcopy(case.inputs)
        call_inputs = copy.deepcopy(case.inputs)
        try:
            actual = getattr(solution_cls(), method_name)(**call_inputs)
            actual = _actual_result(actual, before, call_inputs)
            passed = values_equal(actual, case.expected, tolerance=tolerance)
            results.append(ExampleResult(case=case, actual=actual, passed=passed))
        except Exception as exc:  # noqa: BLE001 - test result should report user-code errors
            results.append(ExampleResult(case=case, error=exc))
    return results


def assert_examples(
    solution_cls: type,
    doc: str | None = None,
    *,
    method_name: str | None = None,
    tolerance: float = 1e-5,
) -> list[ExampleResult]:
    results = run_examples(
        solution_cls,
        doc,
        method_name=method_name,
        tolerance=tolerance,
    )
    failed = [result for result in results if not result.passed]
    if failed:
        raise AssertionError(format_results(failed))
    return results


def format_results(results: Iterable[ExampleResult]) -> str:
    lines = []
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        line = f"{status} example {result.case.index}"
        if result.error is not None:
            line += f": {type(result.error).__name__}: {result.error}"
        elif not result.passed:
            line += f": expected {result.case.expected!r}, got {result.actual!r}"
        lines.append(line)
    return "\n".join(lines)


def load_solution_file(path: str | Path) -> dict[str, Any]:
    source_path = Path(path)
    source = source_path.read_text()
    tree = ast.parse(source, filename=str(source_path))
    module = _without_top_level_demo_expressions(tree)
    ast.fix_missing_locations(module)

    namespace = {
        "__builtins__": __builtins__,
        "__doc__": ast.get_docstring(tree),
        "__file__": str(source_path),
        "__name__": "__leetcode_solution__",
    }
    sys.path.insert(0, str(source_path.parent))
    try:
        exec(compile(module, str(source_path), "exec"), namespace)
    finally:
        try:
            sys.path.remove(str(source_path.parent))
        except ValueError:
            pass
    return namespace


def values_equal(actual: Any, expected: Any, *, tolerance: float = 1e-5) -> bool:
    if isinstance(actual, bool) or isinstance(expected, bool):
        return actual is expected

    if isinstance(actual, int | float) and isinstance(expected, int | float):
        if isinstance(actual, float) or isinstance(expected, float):
            return math.isclose(actual, expected, rel_tol=tolerance, abs_tol=tolerance)
        return actual == expected

    if isinstance(actual, list | tuple) and isinstance(expected, list | tuple):
        return len(actual) == len(expected) and all(
            values_equal(left, right, tolerance=tolerance)
            for left, right in zip(actual, expected, strict=True)
        )

    if isinstance(actual, Mapping) and isinstance(expected, Mapping):
        return actual.keys() == expected.keys() and all(
            values_equal(actual[key], expected[key], tolerance=tolerance)
            for key in actual
        )

    return actual == expected


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run copied LeetCode docstring examples against a Solution class."
    )
    parser.add_argument("path", help="Path to a Python solution file.")
    parser.add_argument("--method", help="Solution method name, if it cannot be inferred.")
    args = parser.parse_args(argv)

    try:
        namespace = load_solution_file(args.path)
        solution_cls = namespace.get("Solution")
        if not isinstance(solution_cls, type):
            raise LeetCodeLocalJudgeError("No Solution class found.")
        results = run_examples(
            solution_cls,
            namespace.get("__doc__"),
            method_name=args.method,
        )
    except LeetCodeLocalJudgeError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(format_results(results))
    return 0 if all(result.passed for result in results) else 1


def _example_blocks(doc: str) -> list[str]:
    lines = doc.replace("\r\n", "\n").splitlines()
    starts = [
        line_no
        for line_no, line in enumerate(lines)
        if line.strip().startswith(_EXAMPLE_HEADER) and line.strip().endswith(":")
    ]
    if not starts:
        return ["\n".join(lines)]

    blocks = []
    for offset, start in enumerate(starts):
        end = starts[offset + 1] if offset + 1 < len(starts) else len(lines)
        blocks.append("\n".join(lines[start:end]))
    return blocks


def _read_section(block: str, label: str) -> str | None:
    lines = block.splitlines()
    collected = None
    for line in lines:
        stripped = line.strip()
        if collected is None:
            if stripped.startswith(label):
                collected = [stripped.removeprefix(label).strip()]
            continue

        if _is_next_section(stripped):
            break
        collected.append(stripped)

    if collected is None:
        return None
    return " ".join(part for part in collected if part).strip()


def _is_next_section(line: str) -> bool:
    return any(line.startswith(label) for label in _SECTION_LABELS)


def _parse_expression(text: str) -> ast.Expression:
    try:
        return ast.parse(text.strip(), mode="eval")
    except SyntaxError as exc:
        raise LeetCodeParseError(f"Could not parse LeetCode literal: {text!r}") from exc


def _literal_eval(node: ast.AST) -> Any:
    normalized = _LeetCodeLiteralNames().visit(node)
    ast.fix_missing_locations(normalized)
    try:
        return ast.literal_eval(normalized)
    except (SyntaxError, ValueError) as exc:
        raise LeetCodeParseError("Unsupported LeetCode literal.") from exc


class _LeetCodeLiteralNames(ast.NodeTransformer):
    def visit_Name(self, node: ast.Name) -> ast.AST:
        if node.id in _NAME_LITERALS:
            return ast.copy_location(ast.Constant(_NAME_LITERALS[node.id]), node)
        return node


def _doc_for(solution_cls: type) -> str | None:
    module = inspect.getmodule(solution_cls)
    if isinstance(module, ModuleType):
        return module.__doc__
    return None


def _solution_method_name(solution_cls: type) -> str:
    names = [
        name
        for name, value in vars(solution_cls).items()
        if not name.startswith("_") and isinstance(value, Callable)
    ]
    if len(names) != 1:
        raise LeetCodeLocalJudgeError(
            "Could not infer Solution method name; pass method_name explicitly."
        )
    return names[0]


def _actual_result(return_value: Any, before: dict[str, Any], after: dict[str, Any]) -> Any:
    if return_value is not None:
        return return_value
    changed_inputs = [name for name, value in after.items() if before[name] != value]
    if len(changed_inputs) == 1:
        return after[changed_inputs[0]]
    raise LeetCodeLocalJudgeError(
        "Solution returned None; expected exactly one mutated input, "
        f"found {len(changed_inputs)}."
    )


def _without_top_level_demo_expressions(tree: ast.Module) -> ast.Module:
    return ast.Module(
        body=[
            node
            for offset, node in enumerate(tree.body)
            if _keep_top_level_node(node, offset)
        ],
        type_ignores=tree.type_ignores,
    )


def _keep_top_level_node(node: ast.stmt, offset: int) -> bool:
    if offset == 0 and _is_docstring_node(node):
        return True
    if isinstance(node, ast.Expr | ast.Raise):
        return False
    if isinstance(node, ast.Assign | ast.AnnAssign):
        return not _references_solution(node.value)
    return True


def _references_solution(node: ast.AST | None) -> bool:
    if node is None:
        return False
    return any(
        isinstance(child, ast.Name) and child.id == "Solution"
        for child in ast.walk(node)
    )


def _is_docstring_node(node: ast.stmt) -> bool:
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(node.value.value, str)
    )


if __name__ == "__main__":
    raise SystemExit(main())
