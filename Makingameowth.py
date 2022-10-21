# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:25:28 2022

@author: Ivar
"""
import math as m
N, P, X, Y = [int(i) for i in input().split()]

intervall = int(P/(N-1))

summ = P*X

summ += intervall*Y

    
print(summ)
    

