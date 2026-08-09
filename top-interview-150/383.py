class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter, defaultdict

        gets = defaultdict(int, Counter(magazine))
        needs = defaultdict(int, Counter(ransomNote))
        for k, v in needs.items():
            if v > gets[k]:
                return False
        return True
