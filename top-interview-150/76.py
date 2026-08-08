class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter, defaultdict

        needs = defaultdict(int, Counter(t))
        total_needs = len(needs)
        gets = defaultdict(int)
        current_gets = 0
        N = len(s)
        L = 0
        min_L, min_R = 0, N - 1
        for R in range(N):
            gets[s[R]] += 1
            if gets[s[R]] == needs[s[R]]:
                current_gets += 1
            if current_gets < total_needs:
                continue
            while gets[s[L]] > needs[s[L]]:
                gets[s[L]] -= 1
                L += 1
            # print(s[L : R + 1])
            if R - L < min_R - min_L:
                min_L, min_R = L, R
        return s[min_L : min_R + 1] if current_gets == total_needs else ""


print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"), "BANC")
print(Solution().minWindow(s="a", t="a"), "a")
print(Solution().minWindow(s="a", t="aa"), "")
