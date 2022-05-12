import sys
import math
import numpy as np
import random
import matplotlib.pyplot as plt
# punkty
# y = b0 + b1x
# mamy x1 i y1 szukamy beta
# robimy z tego macierze i równanie macierze
# maciez X razy b0 i b1 = macierz y
# równania macierzowe za pomoca lewostronnej odwrotnosci
# Xt * X = 1
# dalsze riki cziki na macierzach i mamy wynik
# z wykladu 
# 2 1 
# 5 2
# 7 3
# 8 3
# Beta 0 2/7
# beta 1 5/14

# ostatni wykład 17minuta (04,04,2022)

def funkcjaLiniowa(x, B0, B1):
    return B0 + B1*x


punkty = [
            [2,1],
            [5,2],
            [7,3],
            [8,3]
]

x = [punkty[x][0] for x in range(len(punkty))]
y = [punkty[x][1] for x in range(len(punkty))]

matrixY = np.matrix(y).transpose()

matrixX = [[1, punkty[x][0]] for x in range(len(punkty))]
matrixX = np.matrix(matrixX)

matrixXT = matrixX.transpose()

mXmXT = matrixXT * matrixX

mXmXTinverse = mXmXT**-1

mXtY = matrixXT * matrixY


result = mXmXTinverse*mXtY

funkcja = []
for i in range(9):
    funkcja.append(funkcjaLiniowa(i, float(result[0][0]), float(result[1][0])))   


plt.plot(funkcja)

plt.scatter(x, y)
plt.show()