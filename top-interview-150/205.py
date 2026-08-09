class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        from collections import defaultdict

        s_t = defaultdict(int)
        t_s = defaultdict(int)
        sl = map(ord, s)
        tl = map(ord, t)
        for ss, tt in zip(sl, tl):
            if ss in s_t and s_t[ss] != tt:
                return False
            if tt in t_s and t_s[tt] != ss:
                return False
            s_t[ss] = tt
            t_s[tt] = ss

        for k, v in s_t.items():
            if t_s[v] != k:
                return False
        return True
