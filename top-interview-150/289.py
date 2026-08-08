from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 2: 1->0
        # 3: 0->1
        rows = len(board)
        cols = len(board[0])

        def live_neighbours(i, j):
            ans = 0
            r_from = max(0, i - 1)
            r_to = min(rows - 1, i + 1)
            c_from = max(0, j - 1)
            c_to = min(cols - 1, j + 1)

            for r in range(r_from, r_to + 1):
                for c in range(c_from, c_to + 1):
                    if (r != i or c != j) and is_live(r, c):
                        ans += 1
            return ans

        def is_live(i, j):
            return (
                board[i][j] == 1  # always 1
                or board[i][j] == 2  # previous 1
            )

        def live_to_dead(i, j):
            if not (2 <= live_neighbours(i, j) <= 3):
                board[i][j] = 2

        def dead_to_live(i, j):
            if live_neighbours(i, j) == 3:
                board[i][j] = 3

        def update_cell(i, j) -> None:
            if is_live(i, j):
                live_to_dead(i, j)
            else:
                dead_to_live(i, j)

        for r in range(rows):
            for c in range(cols):
                update_cell(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:  # current 0
                    board[r][c] = 0
                if board[r][c] == 3:  # current 1
                    board[r][c] = 1


def pp(mat):
    rows = cols = len(mat)
    max_val = rows * cols - 1
    max_len = len(str(max_val))
    for row in mat:
        for cell in row:
            cell_str = str(cell)
            cell_len = len(cell_str)
            print(cell_str, end=" " * (max_len - cell_len + 2))
        print()


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
pp(board)
Solution().gameOfLife(board)
print("=" * 20)
pp(board)
