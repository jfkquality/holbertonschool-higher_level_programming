#!/usr/bin/python3
def square_matrix_map(matrix=[]):
        newmatrix = list(map(list, matrix) *(map(list, matrix)))
        # for i, row in enumerate(matrix):
        #     for j, col in enumerate(row):
        #         newmatrix[i][j] = (matrix[i][j] * matrix[i][j])
        # return (newmatrix)
