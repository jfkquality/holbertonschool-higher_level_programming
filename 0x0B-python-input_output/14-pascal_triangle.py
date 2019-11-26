#!/usr/bin/python3
def pascal_triangle(n):
    triangle = [] # or [n]?

    for row in range(n): #or triangle?
        newrow = []
        newrow.append(1)
        for item in range(row):
            newrow.append(item + 1)
        triangle.append(newrow)
    return(triangle)
