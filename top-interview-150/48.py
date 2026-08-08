from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        def transpose():
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def flip_x():
            for i in range(n):
                for j in range(n // 2):
                    matrix[i][j], matrix[i][n - 1 - j] = (
                        matrix[i][n - 1 - j],
                        matrix[i][j],
                    )

        transpose()
        flip_x()


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
            print(cell_str, end=" " * (max_len - cell_len + 1))
        print()


mat_33 = get_mat(3, 3)
pp(mat_33)
Solution().rotate(mat_33)
pp(mat_33)
