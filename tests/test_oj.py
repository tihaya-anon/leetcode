import ast
import tempfile
import textwrap
import unittest
from pathlib import Path

from utils import (
    LeetCodeLocalJudgeError,
    assert_examples,
    load_solution_file,
    parse_examples,
    parse_input,
    parse_value,
    run_examples,
)


class LeetCodeDocstringJudgeTests(unittest.TestCase):
    def test_parses_71_examples_from_docstring(self):
        source = Path("top-interview-150/71.py").read_text()
        examples = parse_examples(ast.get_docstring(ast.parse(source)))

        self.assertEqual(len(examples), 5)
        self.assertEqual(examples[0].inputs, {"path": "/home/"})
        self.assertEqual(examples[0].expected, "/home")
        self.assertEqual(examples[-1].expected, "/.../b/d")

    def test_runs_examples_against_solution_class(self):
        source = Path("top-interview-150/71.py").read_text()
        doc = ast.get_docstring(ast.parse(source))

        class Solution:
            def simplifyPath(self, path: str) -> str:
                stack = []
                for part in path.split("/"):
                    if part in ("", "."):
                        continue
                    if part == "..":
                        if stack:
                            stack.pop()
                    else:
                        stack.append(part)
                return "/" + "/".join(stack)

        results = run_examples(Solution, doc)

        self.assertTrue(all(result.passed for result in results), results)

    def test_supports_leetcode_json_literal_names(self):
        self.assertEqual(
            parse_input("flag = true, missing = null"),
            {"flag": True, "missing": None},
        )
        self.assertEqual(parse_value("[true,false,null]"), [True, False, None])

    def test_supports_in_place_solution_methods(self):
        doc = """
        Example 1:

        Input: matrix = [[1,2],[3,4]]
        Output: [[3,1],[4,2]]
        """

        class Solution:
            def rotate(self, matrix):
                matrix[:] = [[3, 1], [4, 2]]

        assert_examples(Solution, doc)

    def test_none_return_requires_one_mutated_input(self):
        doc = """
        Example 1:

        Input: left = [1], right = [2]
        Output: [1]
        """

        class Solution:
            def ambiguous(self, left, right):
                return None

        result = run_examples(Solution, doc)[0]

        self.assertIsInstance(result.error, LeetCodeLocalJudgeError)

    def test_load_solution_file_skips_top_level_demo_code(self):
        source = textwrap.dedent(
            '''
            """
            Example 1:

            Input: x = 1
            Output: 2
            """

            MOD = 10**9 + 7

            class Solution:
                def plusOne(self, x):
                    return x + 1 + MOD - MOD

            raise RuntimeError("demo code should not run")
            '''
        )

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "demo.py"
            path.write_text(source)

            namespace = load_solution_file(path)
            assert_examples(namespace["Solution"], namespace["__doc__"])


if __name__ == "__main__":
    unittest.main()
