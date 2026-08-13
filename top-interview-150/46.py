from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ret = []
        visit = [0 for _ in nums]

        def dfs(i, path):
            if i == N:
                ret.append(path)
                return
            for idx in range(N):
                if visit[idx]:
                    continue
                visit[idx] = 1
                dfs(i + 1, path + [nums[idx]])
                visit[idx] = 0

        dfs(0, [])
        return ret


print(Solution().permute([2]))
