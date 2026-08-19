from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [0] * n  # dp[i]: max_dis for i step
        last_dp = 0
        cur_dp = 0
        last_dis = 0
        for i in range(1, n):
            pre_dis = last_dp
            cur_dp = max(idx + nums[idx] for idx in range(last_dis, pre_dis + 1))
            # print(i, dp, last_dis, pre_dis)
            if cur_dp >= n - 1:
                return i
            last_dis = pre_dis
            last_dp = cur_dp
        return n - 1


print(Solution().jump([2, 3, 1, 1, 4]))  # 2
print(Solution().jump([2, 3, 0, 1, 4]))  # 2
print(Solution().jump([1, 1, 2, 1, 1]))  # 3
