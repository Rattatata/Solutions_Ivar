# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:52:49 2022

@author: Ivar
"""

X, Y = [int(i)for i in input().split()]


if Y%2 != 0:
    print('impossible')
else:
    print('possible')
