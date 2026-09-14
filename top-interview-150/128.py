from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ret = 0
        for n in nums_set:
            if n - 1 in nums_set:
                continue
            lgth = 1
            nxt = n + 1
            while nxt in nums_set:
                lgth += 1
                nxt += 1
            ret = max(ret, lgth)
        return ret


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
