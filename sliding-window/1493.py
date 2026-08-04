"""
1493. Longest Subarray of 1's After Deleting One Element
Medium
Topics
premium lock icon
Companies
Hint
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        zero_cnt = 0
        l = 0
        maxL = 0
        for r in range(n):
            if nums[r] == 0:
                zero_cnt += 1
            while zero_cnt == 2:
                if nums[l] == 0:
                    zero_cnt -= 1
                l += 1
            curL = r - l + 1
            maxL = max(maxL, curL)
        if l == 0:
            return n - 1
        return maxL - 1


if __name__ == "__main__":
    nums = [1, 1, 1]
    sol = Solution()
    ret = sol.longestSubarray(nums)
    print(ret)
