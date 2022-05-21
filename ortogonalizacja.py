import sys
import math
import numpy as np
import random
import matplotlib.pyplot as plt
from copy import copy
from gaussJardan import GaussJordan
from SIUtility import *





A = [
            [2,0],
            [1,1],
            [0,1]
]

tempVectors = np.matrix(A)
tempVectors = np.transpose(tempVectors)

vectors = np.asarray(np.squeeze(tempVectors))
vectors = vectors.astype('float64')


arrayU = []

for i in range(len(vectors)):
    v = vectors[i]
    suma = sumProj(arrayU, v, i)
    arrayU.append(v-suma)

arrayE = []

for i in range(len(arrayU)):
    arrayE.append(normalize(arrayU[i]))


matrixA = np.matrix(A)
matrixQT = np.matrix(arrayE)
matrixQ = np.transpose(matrixQT)

R = matrixQT*matrixA

#A1 = matrixQT * matrixA * matrixQ
np.set_printoptions(suppress=True)

print(R)


#not working for squared
temparrR= np.array(R)
arrR = []
for i in temparrR:
    arrR.append(i.tolist())


GRResult = GaussJordan(R)

