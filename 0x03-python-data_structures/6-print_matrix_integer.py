#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print('\n'.join([' '.join(['{:d}'.format(item) for item in row])
        for row in matrix]))

    # for row in matrix:
    #     for val in row:
    #         print('{:d}'.format(val), end=' '
    #               if row.index(val) < len(row) - 1 else '')
    #     print()
