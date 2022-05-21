
import sys
import math
import numpy as np
import random
import matplotlib.pyplot as plt
from copy import copy

def normalize(u):
    dot = np.sqrt(np.sum(np.dot(u,u)))
    result = u / dot
    return result

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
