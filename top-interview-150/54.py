from typing import Any, List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        rows = len(matrix)
        cols = len(matrix[0])

        def ring(ul, br):
            # print(ul, br)
            row_top = ul[0]
            row_bottom = br[0]
            col_left = ul[1]
            col_right = br[1]
            if row_top == row_bottom:
                for c in range(col_left, col_right + 1):
                    ans.append(matrix[row_top][c])
                return
            if col_left == col_right:
                for r in range(row_top, row_bottom + 1):
                    ans.append(matrix[r][col_left])
                return
            for c in range(col_left, col_right):
                ans.append(matrix[row_top][c])
            for r in range(row_top, row_bottom):
                ans.append(matrix[r][col_right])
            for c in range(col_right, col_left, -1):
                ans.append(matrix[row_bottom][c])
            for r in range(row_bottom, row_top, -1):
                ans.append(matrix[r][col_left])

        for layer in range((min(rows, cols) + 1) // 2):
            ring([layer, layer], [rows - 1 - layer, cols - 1 - layer])
        return ans


def get_mat(rows, cols) -> tuple[List[List[int]], Any]:
    mat = []
    for i in range(rows):
        row = [i * cols + j for j in range(cols)]
        mat.append(row)

    def pp():
        max_val = rows * cols - 1
        max_len = len(str(max_val))
        for row in mat:
            for cell in row:
                cell_str = str(cell)
                cell_len = len(cell_str)
                print(cell_str, end=" " * (max_len - cell_len + 1))
            print()

    return mat, pp


mat, pp = get_mat(3, 3)
pp()
ret = Solution().spiralOrder(mat)
print(ret)

mat, pp = get_mat(5, 3)
pp()
ret = Solution().spiralOrder(mat)
print(ret)

mat, pp = get_mat(4, 7)
pp()
ret = Solution().spiralOrder(mat)
print(ret)

mat, pp = get_mat(7, 4)
pp()
ret = Solution().spiralOrder(mat)
print(ret)
