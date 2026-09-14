class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0
        for tt in t:
            if s_i == len(s):
                return False
            if tt == s[s_i]:
                s_i += 1
        return s_i == len(s)


print(Solution().isSubsequence("abc", "ahbgdc"))
print(Solution().isSubsequence("axc", "ahbgdc"))
