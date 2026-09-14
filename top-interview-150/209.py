from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        cur_sum = 0
        min_len = len(nums)
        i = -1
        for j, n in enumerate(nums):
            cur_sum += n
            while cur_sum >= target:
                # print(i, j)
                min_len = min(min_len, j - i)
                i += 1
                cur_sum -= nums[i]

        return min_len


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(Solution().minSubArrayLen(4, [1, 4, 4]))
print(Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
print(Solution().minSubArrayLen(11, [1, 2, 3, 4, 5]))
