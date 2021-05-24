#!/usr/bin/env python2
import random
from BatAlgorithm import *

def Fun(D, sol):
    val = 0.0
    for i in range(D):
        val = val + sol[i] * sol[i]
    return val

# For reproducive results
#random.seed(5)

for i in range(10):
    Algorithm = BatAlgorithm(D=10, NP=40, N_Gen=1000, A=0.5, r=0.5, fMin=0.0, fMax=2.0, Lower=-10.0, Upper=10.0, function=Fun)
    Algorithm.move_bat()
