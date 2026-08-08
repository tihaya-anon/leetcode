"""
1004. Max Consecutive Ones III
Medium
Topics
premium lock icon
Companies
Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_len = cur_zeros = 0
        L = 0
        for R in range(n):
            if nums[R] == 0:
                cur_zeros += 1
            while L <= R and cur_zeros > k:
                if nums[L] == 0:
                    cur_zeros -= 1
                L += 1
            # print(cur_zeros, nums[L : R + 1])
            max_len = max(max_len, R - L + 1)
        return max_len


if __name__ == "__main__":
    params = dict(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2)
    ans = 6
    print(Solution().longestOnes(**params), ans)

    params = dict(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3)
    ans = 10
    print(Solution().longestOnes(**params), ans)
