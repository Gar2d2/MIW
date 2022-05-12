import sys
import math
import numpy as np
import random
import matplotlib.pyplot as plt

def obliczSrednia(wektor):
    array = [1 for x in range(len(wektor))]
    return np.dot(array,wektor)/len(wektor)


def wariancja(wektor):
    srednia = obliczSrednia(wektor)
    wektor = [x - srednia for x in wektor]
    wynik = np.dot(wektor,wektor) / len(wektor)
    return wynik

def odchylenieStandardowe(wektor):
    return math.sqrt(wariancja(wektor))
    
print(odchylenieStandardowe([5,7,9]))