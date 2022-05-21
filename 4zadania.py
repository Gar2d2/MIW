# Importing NumPy Library
import numpy as np
import sys
from SIUtility import normalize

#
B = [
    [1, 1, 1, 1,    1, 1, 1, 1],
    [1, 1, 1, 1,   -1,-1,-1,-1],
    [1, 1,-1,-1,    0, 0, 0, 0],
    [0, 0, 0, 0,    1, 1,-1,-1],
    [1,-1, 0, 0,    0, 0, 0, 0],
    [0, 0, 1,-1,    0, 0, 0, 0],
    [0, 0, 0, 0,    1,-1, 0, 0],
    [0, 0, 0, 0,    0, 0, 1,-1],    
]
np.set_printoptions(suppress=True)
#1sprawdzamy czy jest ortogonalna
matrixB = np.matrix(B)
matrixBtranspose = matrixB.transpose()

resultMatrix = matrixB*matrixBtranspose
bIsDiagonal = np.count_nonzero(resultMatrix - np.diag(np.diagonal(resultMatrix))) == 0
print(resultMatrix)
print(bIsDiagonal)

#2 Normalizacja B
Bnorm =[]
for array in B:
    Bnorm.append(normalize(array))

#3sprawdzenie ortonormalnosci
matrixBnorm = np.matrix(Bnorm)
matrixBnormTransposed = matrixBnorm.transpose()
matrixBnormTransposed = matrixBnormTransposed.round(6)
resultMatrix = matrixBnorm*matrixBnormTransposed

identityMatrix = np.identity(len(B))
resultMatrix = resultMatrix.round(2)
bIsIdentity = np.count_nonzero(resultMatrix - identityMatrix) ==0
print(resultMatrix)
print(bIsIdentity)

#4 przeprowadzenie z bazy do bazy

vector = [8, 6, 2, 3, 4, 6, 6, 5]
matrixFromVector = np.matrix(vector).transpose()
vectorInBaseB = matrixBnormTransposed*matrixFromVector
vectorInBaseB = vectorInBaseB.transpose()
print(vectorInBaseB)



