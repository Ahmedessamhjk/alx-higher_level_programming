#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return (None)
    for a in matrix:
        if len(a) == 0:
            print()
        for x in range(len(a)):
            print("{:d}".format(a[x]), end="\n" if x is len(a) - 1 else " ")
