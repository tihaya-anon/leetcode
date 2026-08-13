from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N1, N2, N3 = len(s1), len(s2), len(s3)
        if N1 + N2 != N3:
            return False

        @cache
        def dfs(i, j):
            # s1[:i]+s2[:j]=?s3[:i+j]
            if i == 0 and j == 0:
                return True
            from_s1 = i - 1 >= 0 and dfs(i - 1, j) and s3[i + j - 1] == s1[i - 1]
            from_s2 = j - 1 >= 0 and dfs(i, j - 1) and s3[i + j - 1] == s2[j - 1]
            return from_s1 or from_s2

        dp = [[False for _ in range(N2 + 1)] for _ in range(N1 + 1)]
        dp[0][0] = True
        for i in range(N1+1):
            for j in range(N2+1):
                if i == 0 and j == 0:
                    continue
                from_s1 = i - 1 >= 0 and dp[i - 1][j] and s3[i + j - 1] == s1[i - 1]
                from_s2 = j - 1 >= 0 and dp[i][j - 1] and s3[i + j - 1] == s2[j - 1]
                dp[i][j] = from_s1 or from_s2

        return dp[N1][N2]


print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
