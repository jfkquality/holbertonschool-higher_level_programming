#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # print('\n'.join([''.join(['{:2d}'.format(item) for item in row])
    #                  for row in matrix]))

    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         print('{:d}'.format(matrix[i][j]), end=' '
    #               if j < len(matrix[i]) - 1 else '')
    #     print()

    for row in matrix:
        for val in row:
            print ('{:d}'.format(val), end=' '
                   if row.index(val) < len(row) - 1 else '')
        print()
