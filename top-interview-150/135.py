from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(n):
            if i == 0:
                continue
            if ratings[i] <= ratings[i - 1]:
                continue
            left = candies[i - 1]
            candies[i] = left + 1
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                continue
            if ratings[i] <= ratings[i + 1]:
                continue
            right = candies[i + 1]
            candies[i] = max(candies[i], right + 1)
        print(candies)
        return sum(candies)


print(Solution().candy([1, 0, 2]))  # 5
print(Solution().candy([1, 2, 2]))  # 4
print(Solution().candy([1, 3, 4, 5, 2]))  # 11
