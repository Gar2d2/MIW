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
for i in range(100):
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

#rozpoczynam liczenie V
AtA = mA.transpose()*mA

#nie wiedzieć czemu daje NAN, wiec korzystam z numpajowego (porownywalem wyniki QR z kalkulatorem i sam rozkład działał OK)
Q, R= np.linalg.qr(AtA)
AtAwlasne = Q*R
for i in range(1000):
    Q, R= np.linalg.qr(AtA)

    if i%2 ==0:
        AtAwlasne= Q*R
    else:
        AtAwlasne = R*Q
        
AtAwlasne = AtAwlasne.round(2)
print(AtAwlasne)

lambdaTable = []
AtAwlasne = AtAwlasne.tolist()
for i in range(len(AtA)):
    lambdaTable.append(AtAwlasne[i][i])

VVektorArray = []
#dla każdej lambdy
for i in range(len(lambdaTable)):
    #for counting eigen vectors
    temp = AtA.tolist()
    for j in range(len(temp)):
        #odejmuje lambdy z przekatnej
        temp[j][j] -= lambdaTable[i]

    #robie bardzo brzydko, bo zakladam ze rozwiazan jest inf a moja implementacja tego nie uwzglednia (spada z rowerka przy kwadratowej)
    temp2 = [temp[x] for x in range(len(temp)-1)]

    #tworze wektor z rozwiazaniami (bez x'a)
    tempVector = [1.]
    [tempVector.append(x) for x in GaussJordan(temp2)]
    VVektorArray.append(tempVector)


for i in range(len(VVektorArray)):
    VVektorArray[i] = normalize(VVektorArray[i]).tolist()

#ok mamy wszystkie wektory z V, ale nie wszystkie moze są potrzebne
matrixVT = np.matrix(VVektorArray)
for i in range(len(UVectorArray)):
    if i > len(VVektorArray):
        break
    atMulVec = mA.transpose() * np.matrix(UVectorArray[i]).transpose()
    mRow= (atMulVec.transpose() * 1/sigmaTable[i])
    matrixVT[i] = mRow



print(mA)
print(matrixU)
print(matrixSigma)
print(matrixVT)

