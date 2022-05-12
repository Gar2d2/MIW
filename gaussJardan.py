# Importing NumPy Library
import numpy as np
import sys

# Reading number of unknowns
a = [
    [2,0,1,6],
    [0,1,0,2],
    [1,2,0,2]
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
GaussJordan(a)