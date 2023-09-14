# write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

from copy import deepcopy


def zero_out_row(matrix, row):
    for y in range(0, len(matrix[row])):
        matrix[row][y] = 0
    return matrix


def zero_out_column(matrix, column):
    for x in range(0, len(matrix)):
        matrix[x][column] = 0
    return matrix


def zero_matrix(matrix):
    clone = deepcopy(matrix)
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            if matrix[x][y] == 0:
                clone = zero_out_row(clone, x)
                clone = zero_out_column(clone, y)
    return clone


def zero_matrix_inline(matrix):
    zero_rows = set()
    zero_columns = set()

    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            if matrix[x][y] == 0:
                zero_rows.add(x)
                zero_columns.add(y)

    for x in zero_rows:
        matrix = zero_out_row(matrix, x)
    for y in zero_columns:
        matrix = zero_out_column(matrix, y)


if __name__ == '__main__':
    pass
