"""
668. Kth Smallest Number in Multiplication Table
Hard
Topics
premium lock icon
Companies
Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.



Example 1:


Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.
Example 2:


Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.


Constraints:

1 <= m, n <= 3 * 104
1 <= k <= m * n
"""


def pp(mat):
    max_ele = mat[-1][-1]
    n = len(str(max_ele)) + 1
    for row in mat:
        for col in row:
            col_len = len(str(col))
            print(col, end=" " * (n - col_len))
        print()


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # m<=n
        if m > n:
            m, n = n, m
        L, R = 0, m * n + 1
        while R - L > 1:
            mid = L + R >> 1
            kth = sum((min(mid // (r + 1), n) for r in range(m)))
            if kth < k:
                L = mid
            else:
                R = mid
        return R


print(Solution().findKthNumber(2, 3, 6), 6)
print(Solution().findKthNumber(3, 3, 5), 3)
print(Solution().findKthNumber(45, 12, 471), 312)
