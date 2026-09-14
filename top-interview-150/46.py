from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ret = []
        visited = [False for _ in nums]

        def dfs(path: List[int]):
            if len(path) == N:
                ret.append(path.copy())
                return
            for i in range(N):
                if visited[i]:
                    continue
                path.append(nums[i])
                visited[i] = True
                dfs(path)
                visited[i] = False
                path.pop()

        dfs([])

        return ret


print(Solution().permute([1, 2, 3]))
