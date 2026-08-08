"""
34. Find First and Last Position of Element in Sorted Array
Medium
Topics
premium lock icon
Companies
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        sl, sr = -1, n
        while sr - sl > 1:
            md = sl + sr >> 1
            if nums[md] < target:
                sl = md
            else:
                sr = md
        # print(sl, sr, nums[sl], nums[sr])
        el, er = -1, n
        while er - el > 1:
            md = el + er >> 1
            if nums[md] > target:
                er = md
            else:
                el = md
        # print(el, er, nums[el], nums[er])
        if sr > el:
            return [-1, -1]
        return [sr, el]


if __name__ == "__main__":
    params = dict(nums=[5, 7, 7, 8, 8, 10], target=8)
    print(Solution().searchRange(**params), [3, 4])

    params = dict(nums=[5, 7, 7, 8, 8, 10], target=6)
    print(Solution().searchRange(**params), [-1, -1])

    params = dict(nums=[], target=0)
    print(Solution().searchRange(**params), [-1, -1])
