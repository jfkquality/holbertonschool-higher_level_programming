#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # if __name__ == "__main__":
        newmatrix = list(map(list, matrix))
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                newmatrix[i][j] = (matrix[i][j] * matrix[i][j])
        return (newmatrix)
