from typing import List


def pp(board):
    for row in board:
        print(" ".join(map(lambda x: f"{x:<2}", row)))


def print_dp(dp):
    N = len(dp) - 1
    from math import sqrt

    n = int(sqrt(N))
    board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, N + 1):
        r, c = num_to_pos(i, n)
        board[r][c] = dp[i]
    print("-" * 20)
    pp(board)
    print("-" * 20)


def num_to_pos(num, n):
    num -= 1
    row = num // n
    col = num % n
    row = n - 1 - row
    if row % 2 == 0:
        col = n - 1 - col
    return row, col


def get_end(n):
    if n % 2 == 1:
        return n * n
    return n * (n - 1) + 1


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from collections import deque

        n = len(board)
        target = n * n

        def num_to_pos(num: int) -> tuple[int, int]:
            quotient, col = divmod(num - 1, n)
            row = n - 1 - quotient

            # 从底部数：第 0 行从左向右，第 1 行从右向左
            if quotient % 2 == 1:
                col = n - 1 - col

            return row, col

        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            current, steps = queue.popleft()

            for rolled in range(current + 1, min(current + 6, target) + 1):
                row, col = num_to_pos(rolled)
                destination = board[row][col] if board[row][col] != -1 else rolled

                if destination == target:
                    return steps + 1

                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, steps + 1))

        return -1


# print(num_to_pos(2, 6))
# print(pos_to_num(*num_to_pos(2, 6), 6))
# print(num_to_pos(11, 6))
# print(pos_to_num(*num_to_pos(11, 6), 6))
# print(num_to_pos(22, 6))
# print(pos_to_num(*num_to_pos(22, 6), 6))
# print(num_to_pos(31, 6))
# print(pos_to_num(*num_to_pos(31, 6), 6))
board = [
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1],
]

print(Solution().snakesAndLadders(board))
