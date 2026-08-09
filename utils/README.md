# LeetCode local judge helpers

`utils.oj` runs examples copied in a solution file's module `__doc__`.

Existing packages I found before implementing this cover adjacent workflows:

- `leetcode-local-tester` fetches/generates LeetCode test scaffolding and needs a
  LeetCode login or cookie for some flows.
- `pyleet` runs solution files against separate `.txt` or `.json` testcase files.
- `python-leetcode-runner` expects manually written `tests = [...]` data in the
  solution file.

This project already stores copied LeetCode descriptions in stable module
docstrings, so the local helper parses `Input:` / `Output:` examples directly
from `__doc__` and does not add a dependency.

Run one file:

```sh
uv run python -m utils top-interview-150/71.py
```

Or use it inside a solution file:

```python
if __name__ == "__main__":
    from utils import assert_examples

    assert_examples(Solution, __doc__)
```
