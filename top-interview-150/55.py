from math import inf
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dis = 0
        N = len(nums)
        for i, n in enumerate(nums):
            if i > max_dis:
                return False
            cur_dis = i + n
            max_dis = max(max_dis, cur_dis)
            if max_dis >= N - 1:
                return True
        return False


print(Solution().canJump([2, 3, 1, 1, 4]))
print(Solution().canJump([3, 2, 1, 0, 4]))
