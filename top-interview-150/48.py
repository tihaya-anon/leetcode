from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        def swap(point_a, point_b):
            x_a, y_a = point_a
            x_b, y_b = point_b
            matrix[x_a][y_a], matrix[x_b][y_b] = matrix[x_b][y_b], matrix[x_a][y_a]

        def transpose():
            for i in range(n):
                for j in range(i + 1, n):
                    swap((i, j), (j, i))

        def flip_x():
            for i in range(n):
                for j in range(n // 2):
                    swap((i, j), (i, n - 1 - j))

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
print()
pp(mat_33)
