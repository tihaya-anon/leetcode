"""
1695. Maximum Erasure Value
Medium
Topics
premium lock icon
Companies
Hint
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).



Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].


Constraints:

1 <= nums.length <= 105
1 <= nums[R] <= 104
"""

from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        from collections import defaultdict

        freq = defaultdict(int)
        cur_sum = max_sum = 0
        L = 0
        for R, num in enumerate(nums):
            # [L, R]
            cur_sum += num
            freq[num] += 1
            while L <= R and freq[num] > 1:
                rm_num = nums[L]
                cur_sum -= rm_num
                freq[rm_num] -= 1
                L += 1
            # print(nums[L : R + 1])
            max_sum = max(max_sum, cur_sum)
        return max_sum


if __name__ == "__main__":
    nums = [4, 2, 4, 5, 6]
    sol = Solution()
    ans = 17
    ret = sol.maximumUniqueSubarray(nums)
    print(ret, ans)
