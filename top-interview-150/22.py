from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ret = []

        def dfs(l, r, s):
            if len(s) == 2 * n:
                ret.append(s)
            if l < n:
                dfs(l + 1, r, s + "(")
            if l > r:
                dfs(l, r + 1, s + ")")

        dfs(0, 0, "")

        return ret


print(Solution().generateParenthesis(3))
