from ortogonalizacja import *

InputA = [
        [1,2,0],
        [2,0,2]
    ]
np.set_printoptions(suppress=True)

#tworze macierze
mA = np.matrix(InputA)
mU = mA*mA.transpose()
#rozpoczynam zabawe z macierzą U
U = np.asarray(mU)

mQ = mU
mR = mU

#próbuje wyznaczyć wartości własne za pomocą QR refactora
arr = QRFactor(U)
R = arr[0]
Q = arr[1]

A = Q*R

#nie wiem jak ale to faktycznie działa (jak bedę miał czas to się dowiem)
for i in range(1000):
    arr = QRFactor(A)
    R = arr[0]
    Q = arr[1]
    if i%2 ==0:
        A = Q*R
    else:
        A = R*Q
A = A.round(2)

#robie tabele z miejscami zerowymi
lambdaTable = []
ArrayA = A.tolist()
for i in range(len(A)):
    lambdaTable.append(ArrayA[i][i])
sigmaTable = [math.sqrt(x) for x in lambdaTable]

# print(R)
# print(Q)
# print(A)

UVectorArray = []
#dla każdej lambdy
for i in range(len(lambdaTable)):
    #for counting eigen vectors
    temp = mU.tolist()
    for j in range(len(temp)):
        #odejmuje lambdy z przekatnej
        temp[j][j] -= lambdaTable[i]

    #robie bardzo brzydko, bo zakladam ze rozwiazan jest inf a moja implementacja tego nie uwzglednia (spada z rowerka przy kwadratowej)
    temp2 = [temp[x] for x in range(len(temp)-1)]

    #tworze wektor z rozwiazaniami (bez x'a)
    tempVector = [1.]
    [tempVector.append(x) for x in GaussJordan(temp2)]
    UVectorArray.append(tempVector)

for i in range(len(UVectorArray)):
    UVectorArray[i] = normalize(UVectorArray[i])

sigma = np.zeros_like(InputA)

for j in range(len(sigma)):
        #odejmuje lambdy z przekatnej
        sigma[j][j] += sigmaTable[j]

matrixU = np.matrix(UVectorArray)
matrixUT = matrixU.transpose()
matrixSigma = np.matrix(sigma)


print(mA)
print(matrixU)
print(matrixSigma)