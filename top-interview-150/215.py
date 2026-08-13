from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k -= 1

        def partition(l, r):
            # [l, r)
            pivot = nums[l + r >> 1]
            hi = [n for n in nums[l:r] if n > pivot]
            eq = [n for n in nums[l:r] if n == pivot]
            lo = [n for n in nums[l:r] if n < pivot]
            new_nums = hi + eq + lo
            for i, n in enumerate(new_nums):
                nums[l + i] = n
            return l + len(hi), l + len(hi) + len(eq)

        L, R = 0, len(nums)
        while L < R:
            l, r = partition(L, R)
            if k < l:
                R = l
            elif l <= k < r:
                return nums[k]
            elif k >= r:
                L = r


s = Solution()
print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
print(s.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
