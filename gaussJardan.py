# Importing NumPy Library
import numpy as np
import sys

#TODO - implement way to solve infinite solutions equasion by removing one of rows
# Reading number of unknowns
a = [
    [1,2],
    # [2,-1],
]
def GaussJordan(a):
    n = len(a)
    x = np.zeros(n)

    for i in range(n):
        for j in range(n):
            if i != j:
                ratio = a[j][i]/a[i][i]

                for k in range(n+1):
                    a[j][k] = a[j][k] - ratio * a[i][k]


    for i in range(n):
        x[i] = a[i][n]/a[i][i]

    return x
print(GaussJordan(a))