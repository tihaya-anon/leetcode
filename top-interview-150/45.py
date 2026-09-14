from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        near = far = jumps = 0
        last = len(nums) - 1
        while far < last:
            farthest = 0
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            near = far + 1
            far = farthest
            jumps += 1
        return jumps


print(Solution().jump([2, 3, 1, 1, 4]))  # 2
print(Solution().jump([2, 3, 0, 1, 4]))  # 2
print(Solution().jump([1, 1, 2, 1, 1]))  # 3
