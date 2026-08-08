from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        rows = defaultdict(set)
        cols = defaultdict(set)
        zones = defaultdict(set)
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue
                zone_x = i // 3
                zone_y = j // 3
                z = zone_x * 3 + zone_y
                if cell in rows[i] or cell in cols[j] or cell in zones[z]:
                    return False
                rows[i].add(cell)
                cols[j].add(cell)
                zones[z].add(cell)
        return True
