# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:49:57 2022

@author: Ivar
"""

CPR = input()
CPR = CPR.replace('-', '')
scalars = [4,3,2,7,6,5,4,3, 2, 1]
value = 0
for val, scal in zip(CPR, scalars):
    value += int(val)*scal

if value % 11 == 0:
    print(1)
else:
    print(0)

