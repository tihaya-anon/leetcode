from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        inf = 10010
        for r_i, r in enumerate(triangle):
            if r_i == 0:
                continue
            for c_i, c in enumerate(r):
                pa_l, pa_r = inf, inf
                if c_i > 0:
                    pa_l = triangle[r_i - 1][c_i - 1]
                if c_i < r_i:
                    pa_r = triangle[r_i - 1][c_i]
                triangle[r_i][c_i] = min(pa_l, pa_r) + c
        return min(triangle[-1])


s = Solution()
print(s.minimumTotal(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]), 11)
