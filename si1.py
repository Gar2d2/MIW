import sys
import math
import numpy as np
import random
# value = input("Podaj imie:\n")

# # print(f'Czesc {value}')
# zmiennaString = "xDDD"
# zmiennaCalkowita = 1
# zmiennaflt = 1.0
# # print("Ceść {}".format(value))
# print(f"""zmienna 1: {zmiennaString}, {type(zmiennaString)},
# zmienna 2: {zmiennaCalkowita}, {type(zmiennaCalkowita)},
# zmienna 3: {zmiennaflt}, {type(zmiennaflt)}""")
# zmienna = ["Slowo1", "slowo2", "slowo3"]

# zmienna2 = "Metody Inżynierii Wiedzy Są Najlepsze"

# print("{0} znaki {1}: ".format(zmienna2.lower(), len(zmienna2)))
# print(zmienna2)

# zmienna2 = zmienna2.replace("ż", "z").replace("ą", "a").replace(" ","")
# print("{0} znaki {1}: ".format(zmienna2, len(zmienna2)))

# set2  = set(zmienna2)
# print("{0} znaki {1}: ".format(set2, len(set2)))
# pair = ("XD", 2)
# print("{0} znaki {1}: ".format(pair, type(pair)))
# listaJen = ["c","c++","python"]
# print(listaJen.index('python'))

# zmienna = ["Slowo1", "slowo2", "slowo3"]

# zmienna2 = ["Slowo4", "slowo5", "slowo6"]

# print("{0} zmienna1/2 {1}, zmienna3: {2}: ".format(zmienna, zmienna2, zmienna+zmienna2))

# diction = {"ukraina" : "moskwa", "polska":"warszawa"}
# print(print(bool(0)))
# #ZADANIE - wymyśleć se zdanie i napisać z ifem taki warunek że sprawdza czy jest wiecej niz 15 znakow w tym ciagu
# zdanie = "chuckles im in danger im over 18 and under 40"
# set1 = set(zdanie)
# if len(set1) > 15:
#     print("wincej")

# string =  "napis#z#haszami#w#srodku"

# def IsPasswordOk(password):

#     if len(password)<10:
#         return False

#     if password.lower() == password:
#         return False

#     if password.upper() == password:
#         return False

#     if password.find('!') == -1:
#         return False

#     return True

# print(IsPasswordOk("12YYYYYyYYYY!"))

# lista = [1,4,6,99,0]

# def CzyNalezy(lista, liczba):
#     i =0
#     result = False

#     while i < len(lista):
#         if lista[i] == liczba:
#             result = True
#             break
#         i+=1

#     return result

# print(CzyNalezy(lista, 9))

# lista = ["c++","c","python"]


# with open('fileNew.txt', 'w') as f:
#     for word in lista:
#         print(word, file = f)
   
# f = open("fileNew.txt", "r")
# for line in f:
#     print(line,end=" ")

# f.close()

# lista = ["olsztyn", "warszawa", "krakow", "lodz"]
# lam = lambda a : a[:3]#print("{0}{1}{2}, ".format(a[0],a[1],a[2]))

# squared_numbers_iterator  = map(lam, lista)

# squared_numbers = list(squared_numbers_iterator)
# print(squared_numbers)
# lista = ["olsztyn.jpg", "warszawa.jpg", "krakow.xD", "lodz.png"]

# def FindFile(arr, extension):
#     for item in arr:
#         if item.endswith(extension):
#             yield item

# ext = list(FindFile(lista, ".jpg"))
# print(ext)


#zadanie domowe - przesłuchać wykład i przesłuchać 
lista = []
f = open("australian.dat", "r")
for line in f:
    
    listaStr = line.split(' ')

    a = lambda x : float(x)
    listaNum = list(map(a, listaStr))
    lista.append(listaNum)

# print(lista)
f.close()

def odlg(lista1, lista2):
    wynik=0

    for i in range(len(lista1) -1):
        wynik += (lista1[i]-lista2[i])**2

    return math.sqrt(wynik)

#print(odlg(lista[0],lista[1]))

#y=lista[0]
#odlg(y,x) gdzie x nalezy do listy bez indeksu 0
#czyli policzycz wszystkie odleglosci miedzy 0 a pozostałymi
#robimy z tego slownik
#klucz to klasa decyzyjna a wartosc - lista z odleglosciami
#klasa decyzyjna jest na ostatnim miejscu w liście
#czyli liczymy od 0 do listy x, i zapisujemy w zależności od tego na końcu do 0 albo 1

#olliczanie wyznacznika macierzy kwadratowej

# lengthDictionary = {}
# lengthDictionary.setdefault('1', [])
# lengthDictionary.setdefault('0', [])

# for i in range(1, len(lista)):
#     lastValue = lista[i][-1]
#     if lastValue == 1:
#         lengthDictionary['1'].append(odlg(lista[0],lista[i]))
#     else:
#         lengthDictionary['0'].append(odlg(lista[0],lista[i]))

# print(lengthDictionary)


    

def GetNearestK(lengthDict, k):
    newDict = {}
    for key in lengthDict:
        if key not in newDict:
            newDict.setdefault(key, [])

        valueList = lengthDict[key]
        valueList.sort()
        newDict[key] = sum(valueList[0:k])

    return newDict

arrayOf1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
arrayOf2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

def WyplujDecyzjeXD(k, listaOdleg):
    tulpa = []
    for i in range(0, len(lista)):
        lastValue = lista[i][-1]
        tulpa.append((lista[i][-1], odlg(lista[i],listaOdleg)))


    lengthDictionary = {}
    lengthDictionary.setdefault('1', [])
    lengthDictionary.setdefault('0', [])

    for value in tulpa:
        if value[0] == 1:
            lengthDictionary['1'].append(value[1])
        else:
            lengthDictionary['0'].append(value[1])

    arrayOfTulpes  = GetNearestK(lengthDictionary, k)
    
    outKey = list(lengthDictionary.keys())[0]
    acctualSmallestValue = arrayOfTulpes[outKey]
    for tulpe in arrayOfTulpes:
        if arrayOfTulpes[tulpe] < acctualSmallestValue:
            acctualSmallestValue = arrayOfTulpes[tulpe]
            outKey = tulpe
    count =0
    for tulpe in arrayOfTulpes:
        if arrayOfTulpes[tulpe] == acctualSmallestValue:
            count +=1
            if count >2:
                return None

    return outKey

# print(WyplujDecyzjeXD(5, arrayOf1))

def metryka(lista1, lista2, utnij = True):
    if utnij:
        v1 = np.array(lista1[:-1])
        v2 = np.array(lista2[:-1])
    else:
        v1 = np.array(lista1)
        v2 = np.array(lista2)
    c = v1-v2
    wynik = math.sqrt(np.dot(c,c))
    return wynik
    
# print(odlg(arrayOf1, arrayOf2))
# print(metryka(arrayOf1,arrayOf2))

# funkcja która zwraca decyzje
# print(lengthDictionary)
# do domu  nagranie z 28 lutego 1h:10 min

listaList = [[1,2,3], [1,2,3],
            [1,1,3], [1,2,3],
            [1,1,3], [1,2,3],
            [1,1,3], [1,2,3],
            [1,1,3], [1,2,3],]

def wyznaczSrodekMasy(glownaListaList):
    #liczymy odleglosci 
    #nie zmieniamy tej listy
    klasaIndex = {}
    for i in range(len(glownaListaList)):
        if glownaListaList[i][-1] not in klasaIndex.keys():
            klasaIndex.setdefault(glownaListaList[i][-1], [])
        klasaIndex[glownaListaList[i][-1]].append(i)
    #tworzymy slownik - klasa decyzyjna, index na liście
    for klasa in klasaIndex:
        listaOldeglosci = []
    print(klasaIndex)
    # na podstawie słownika liczymy oldegłości

    # index z najmniejszymo



def koloruj(glownaListaList, iloscKlas):
    #mamy liste list
    #losowo nadajemy kolory - klase decyzyjną
    for lista in glownaListaList:
        lista[-1] = random.randrange(0,iloscKlas)

    wyznaczSrodekMasy(glownaListaList)
    # print(glownaListaList)
    #wyznaczamy środeki masy grup

    #iterujemy po wszystkich kropkach i sprawdzamy do którego środka masy ma bliżej i nadajemy im taki kolor

    #znowu dzielimy na grupy, i powtażamy sytuacje, algorytm działa dopóki są jakieś zmiany w kolorze

koloruj(listaList,2)


#kolejne 2 zadania do domu
# zrobić obszar z całki, zabaźgać punktów sprawdzić ile jest nad krzywą a ile pod, dostaniemy proporcje, i możymy przez pole, dostajemy całke
# napisać funkcje która będzie całkowała metodą monte carlo

#2gie zadanie, całkowanie metodą 
#dzielimy funkcje na przedziały, robimy prostokąty z tych przedziałów, liczymy pole