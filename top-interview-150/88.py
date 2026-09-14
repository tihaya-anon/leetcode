from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        iter_1 = m - 1
        iter_2 = n - 1
        iter_ret = m + n - 1
        while iter_ret >= 0 and iter_1 >= 0 and iter_2 >= 0:
            if nums1[iter_1] > nums2[iter_2]:
                nums1[iter_ret] = nums1[iter_1]
                iter_1 -= 1
            else:
                nums1[iter_ret] = nums2[iter_2]
                iter_2 -= 1
            iter_ret -= 1
        while iter_ret >= 0 and iter_1 >= 0:
            nums1[iter_ret] = nums1[iter_1]
            iter_1 -= 1
            iter_ret -= 1
        while iter_ret >= 0 and iter_2 >= 0:
            nums1[iter_ret] = nums2[iter_2]
            iter_2 -= 1
            iter_ret -= 1
        print(nums1)


Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
Solution().merge(nums1=[1], m=1, nums2=[], n=0)
Solution().merge(nums1=[0], m=0, nums2=[1], n=1)
