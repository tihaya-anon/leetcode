class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        adds = set()

        def check(r, c):
            for x, y in adds:
                if r == x or c == y:
                    return False
                dx = r - x
                dy = c - y
                if dx == dy or dx == -dy:
                    return False
            return True

        def dfs(r):
            nonlocal ans
            if r == n:
                ans += 1
                return
            for c in range(n):
                if check(r, c):
                    adds.add((r, c))
                    dfs(r + 1)
                    adds.remove((r, c))

        dfs(0)
        return ans


print(Solution().totalNQueens(4))
