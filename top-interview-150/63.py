from typing import List


def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        obstacleGrid[0][0] = 1
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = -1
                    continue
                up = 0
                if r > 0 and obstacleGrid[r - 1][c] != -1:
                    up = obstacleGrid[r - 1][c]
                left = 0
                if c > 0 and obstacleGrid[r][c - 1] != -1:
                    left = obstacleGrid[r][c - 1]
                obstacleGrid[r][c] = up + left
                # print(r, c)
                # print_grid(obstacleGrid)
                # print("=" * 10)
        last = obstacleGrid[-1][-1]
        if last == -1:
            return 0
        return last


ret = Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
print(ret)
