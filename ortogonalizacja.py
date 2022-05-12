import sys
import math
import numpy as np
import random
import matplotlib.pyplot as plt
from copy import copy
# u1 = v1
# e1 = u1/||u1||
# u2 = v2 - proju1(v2)
# e2 = u2/||u2||
#R = Q^T A


def proj(u, v):
    temp = u
    cos = (np.dot(v,temp)/np.dot(temp,temp))
    for i in range(len(temp)):
        temp[i] = temp[i]* cos
    return temp

def sumProj(tabU, vector, liczbaProjekcji):
    result =[]
   
    for j in range(len(vector)):
        result.append(0)
    
    for i in range(liczbaProjekcji):
        u = copy(tabU[i])
        temp = proj(u, vector)
        result = result+temp
    return result

def normalize(u):
    dot = np.sqrt(np.sum(np.dot(u,u)))
    result = u / dot
    return result

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
