#!/usr/bin/python3


def pascal_triangle(n):
    """
    Print the triangle up to the nth row
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1] + [prev-row[i] + prev_row[i + 1] for j
                         in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle
