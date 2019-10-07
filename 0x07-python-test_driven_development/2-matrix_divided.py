#!/usr/bin/python3
def matrix_divided(matrix, div):
        newmatrix = []

        if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
        if div == 0:
                raise ZeroDivisionError("division by zero")
        prevlen = len(matrix[0])
        for i, row in enumerate(matrix):
                if len(matrix[i]) != prevlen:
                        raise TypeError("Each row of the matrix\
                        must have the same size")
                prevlen = len(matrix[i])
        for j, row in enumerate(matrix):
                newmatrix.append([])
                for k, val in enumerate(row):
                        # if not all(isinstance(row, (int, float)) for i in row
                        if not isinstance(val, (int, float)):
                                raise TypeError("matrix must be a matrix\
                                (list of lists) of integers/floats")
                        val = int((100 * (val / div) - .5) + 1) / 100.00
                        newmatrix[j].append(val)
        return newmatrix
