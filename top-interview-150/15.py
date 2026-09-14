class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        ret = []
        nums.sort()

        def two_sum(start, end, target):
            # [start, end]
            i, j = start, end
            _ret = []
            while i < j:
                cur = nums[i] + nums[j]
                if cur > target:
                    j -= 1
                elif cur < target:
                    i += 1
                else:
                    _ret.append([i, j])
                    i += 1
                    j -= 1
            return _ret

        for i, n in enumerate(nums):
            _ret = two_sum(i + 1, N - 1, -n)
            if len(_ret) == 0:
                continue
            for j, k in _ret:
                ret.append((nums[i], nums[j], nums[k]))

        return list(map(list, set(ret)))


print(Solution().threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum(nums=[0, 1, 1]))
print(Solution().threeSum(nums=[0, 0, 0]))
