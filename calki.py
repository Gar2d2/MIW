import random
import numpy as np
import matplotlib.pyplot as plt

# prostokatne
def prostokat(x, y):
    return x*y

def f(x):
    return x

def findMax(x1, x2):
    if x1 > x2:
        return x1
    else:
        return x2

def calkaProsto(start,end, liczbaPodzialow,function):
    wynik = []
    for i in range(0, end +1):
        wynik.append(function(i))   

    plt.plot(wynik)
    plt.axvline(start, color='red', ls='-')
    plt.axvline(end, color='red', ls='-')

    podzialy = [end, start]
    for i in range(liczbaPodzialow):
        podzialy.sort()
        for j in range(len(podzialy)-1):
            x = (podzialy[j] + podzialy[j+1])/2
            podzialy.append(x)
        podzialy.sort()
    sumaPola = 0
    for i in range(len(podzialy)-1):
        sumaPola += prostokat(podzialy[i+1]-podzialy[i], findMax(f(podzialy[i]), f(podzialy[i+1])))
    for i in range( len(podzialy)-1):
        plt.vlines(x=podzialy[i], ymin=0, ymax=f(podzialy[i+1]), colors='green')

    for i in range(1, len(podzialy)):
        plt.hlines(function(podzialy[i]), podzialy[i-1], podzialy[i],colors='green')

    tabelaZy = []
    plt.show()
    return sumaPola


def makeADot(xk, xp, maxVal):
    x = random.uniform(xk, xp)
    y = random.uniform(0, maxVal)
    return (x,y)


def monteCarlo(start, end,kropki, function):

    funkcja = []
    for i in range(0, end+1):
        funkcja.append(function(i))   
    plt.plot(funkcja)
    plt.axvline(start, color='red', ls='--')
    plt.axvline(end, color='red', ls='--')
    maxVal = -float('inf')
    for i in range(start, end+1):
        if(f(i) > maxVal):
            maxVal = function(i)
    under = 0
    for i in range(kropki):
        dot = makeADot(start, end, maxVal*2)
        if(dot[1] < function(dot[0])):
            under += 1
            plt.plot(dot[0], dot[1], 'ro', color='g')
        else:
            plt.plot(dot[0], dot[1], 'ro', color='y')
    pole = prostokat(end-start, maxVal*2)
    plt.show()
    wynik = pole * (under/kropki)
    print(wynik)


        

print(monteCarlo(0,1,4,f))
# print(calkaProsto(0,1,14,f))