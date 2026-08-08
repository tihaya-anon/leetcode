# Binary Search Template

Use this template when the predicate is monotonic:

```text
True True True ... True False False ... False
```

The goal is to find the boundary between the last `True` position and the
first `False` position.

```python
l, r = -1, n

while r - l > 1:
    m = (l + r) // 2

    if check(m):
        l = m
    else:
        r = m
```

At the end:

```text
r - l == 1
l = last index where check(i) is True
r = first index where check(i) is False
```

The sentinels `l = -1` and `r = n` mean the answer may be outside the array:

```text
l == -1  -> no valid index passes check
r == n   -> no valid index fails check
```

## Invariant

Throughout the loop:

```text
-1 <= l < r <= n
all valid indices i <= l pass check
all valid indices i >= r fail check
```

Initially, `l = -1` and `r = n`, so both known ranges are empty. Therefore the
invariant holds vacuously.

During each iteration, the loop condition gives:

```text
r - l > 1
```

So the midpoint satisfies:

```text
l < m < r
```

If `check(m)` is `True`, then by monotonicity every valid index `i <= m` also
passes `check`, so assigning `l = m` preserves the invariant.

If `check(m)` is `False`, then by monotonicity every valid index `i >= m` also
fails `check`, so assigning `r = m` preserves the invariant.

## Termination

Each iteration strictly shrinks the interval because `m` is strictly between
`l` and `r`. Since `r - l` is a positive integer, the loop must eventually end.

When the loop exits:

```text
r - l <= 1
```

But the invariant still gives:

```text
l < r
```

So:

```text
r - l >= 1
```

Combining both facts:

```text
r - l == 1
```

## Sorted Array Examples

Assume `seq` is sorted in nondecreasing order.

### Lower Bound

```python
check = lambda i: seq[i] < target
```

Final meaning:

```text
l = last index where seq[i] < target
r = first index where seq[i] >= target
```

So `r` is the lower bound of `target`.

### Upper Bound

```python
check = lambda i: seq[i] <= target
```

Final meaning:

```text
l = last index where seq[i] <= target
r = first index where seq[i] > target
```

So `r` is the upper bound of `target`.
