import sys
import math
import numpy as np
import random
import matplotlib.pyplot as plt

lista = []
f = open("australian.dat", "r")
for line in f:
    
    listaStr = line.split(' ')

    a = lambda x : float(x)
    listaNum = list(map(a, listaStr))
    lista.append(listaNum)

# print(lista)
f.close()

def makeADot(xk, xp, maxVal):
    x = random.uniform(xk, xp)
    y = random.uniform(0, maxVal)
    return [x,y,0]
listaList =[]

for i in range(200):
    listaList.append(makeADot(0,100,100))
# listaList = [
#             [1,1,3], [1,2,3], [1,3,3], [1,4,3],
#             [2,1,3], [2,2,3], [2,3,3], [2,4,3],
#             [3,1,3], [3,2,3], [3,3,3], [3,4,3],
#             [4,1,3], [4,2,3], [4,3,3], [4,4,3],
#             [5,1,3], [5,2,3], [5,3,3], [5,4,3]]




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

def znajdzNajmniejszy(lista):
    najmniejszy=0
    najmniejszaWartosc = lista[0]
    for i in range(len(lista)):
        if lista[i] < najmniejszaWartosc:
            najmniejszy =i
            najmniejszaWartosc = lista[i]
    return najmniejszy

def wyznaczSrodkiMasy(glownaListaList):
    #liczymy odleglosci 
    #nie zmieniamy tej listy
    #tworzymy slownik - klasa decyzyjna, index na liście
    klasaIndex = {}
    klasaIndexSrodek = {}
    for i in range(len(glownaListaList)):
        if glownaListaList[i][-1] not in klasaIndex.keys():
            klasaIndex.setdefault(glownaListaList[i][-1], [])
        klasaIndex[glownaListaList[i][-1]].append(i)
    #iterujemy po kluczach i wyznaczamy srodek ciezkosci
    for klasa in klasaIndex:
        listaOldeglosci = []

        #wyznaczamy dla każdego indexu odleglosci do kolejnych i appendujemy do listy
        for index in klasaIndex[klasa]:
            listaOdlgDlaIndexu = []
            for index2 in klasaIndex[klasa]:
                listaOdlgDlaIndexu.append(metryka(glownaListaList[index], glownaListaList[index2]))
            listaOldeglosci.append(sum(listaOdlgDlaIndexu))

        #znajdź index z najmniejszą wartością
        klasaIndexSrodek.setdefault(klasa,[])

        najmniejszyIndex = znajdzNajmniejszy(listaOldeglosci)
        klasaIndexSrodek[klasa].append(klasaIndex[klasa][najmniejszyIndex])
        print(najmniejszyIndex)

    return klasaIndexSrodek
    # index z najmniejszymo

def kolorujPoSrodkachMasy(glownaListaList, indexySrodkow):
    bBylaZmiana = False
    for lista in glownaListaList:
        listaOdleglosci = []
        for klasa in indexySrodkow:
            listaOdleglosci.append(metryka(glownaListaList[indexySrodkow[klasa][0]], lista))
        najblizejDo = znajdzNajmniejszy(listaOdleglosci)
        nowaKlasa = list(indexySrodkow.keys())[najblizejDo] #mamy nową klase teraz kolorujemy

        if nowaKlasa != lista[-1]:
            bBylaZmiana = True
        lista[-1] = nowaKlasa

    return bBylaZmiana

def koloruj(glownaListaList, iloscKlas):
    #mamy liste list
    #losowo nadajemy kolory - klase decyzyjną
    for lista in glownaListaList:
        lista[-1] = random.randrange(0,iloscKlas)

    # srodkiMasy = wyznaczSrodkiMasy(glownaListaList)

    bBylaZmiana = True
    while bBylaZmiana == True:

        #wyznaczamy środeki masy grup
        srodkiMasy = wyznaczSrodkiMasy(glownaListaList)
        bBylaZmiana = kolorujPoSrodkachMasy(glownaListaList,srodkiMasy)

        #kolorujemy na podstawie srodkow masy
    print("KONIEC")
    x = []
    y = []
    c = []
    for lista in glownaListaList:
        x.append(lista[0])
        y.append(lista[1])
        c.append(lista[-1])



    plt.scatter(x, y, c=c)
    plt.show()
    #iterujemy po wszystkich kropkach i sprawdzamy do którego środka masy ma bliżej i nadajemy im taki kolor

    #znowu dzielimy na grupy, i powtarzamy sytuacje, algorytm działa dopóki są jakieś zmiany w kolorze

koloruj(listaList,3)
