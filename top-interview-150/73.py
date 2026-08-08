from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # check 1st row
        first_row_has_zero = False
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break

        # check 1st col
        first_col_has_zero = False
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break

        # mark zeros using 1st row & 1st col
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        # set row to zero
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(cols):
                    matrix[r][c] = 0

        # set col to zero
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(rows):
                    matrix[r][c] = 0

        # set 1st row to zero if needed
        if first_row_has_zero:
            for c in range(cols):
                matrix[0][c] = 0

        # set 1st col to zero if needed
        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0


def get_mat(rows, cols) -> List[List[int]]:
    mat = []
    for i in range(rows):
        row = [i * cols + j + 1 for j in range(cols)]
        mat.append(row)
    return mat


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


mat = get_mat(3, 4)
mat[0][0] = 0
mat[0][3] = 0
pp(mat)
Solution().setZeroes(mat)
print("-" * 20)
pp(mat)
