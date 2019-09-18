#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print('\n'.join([''.join(['{:2}'.format(item) for item in row])
                     for row in matrix]))

    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         print('{:2}'.format(matrix[i][j]), end=''),
    #     print()

    # for row in matrix:
    #     for val in row:
    #         print ('{:2}'.format(val), end='')
    #     print()
