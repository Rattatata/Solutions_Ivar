# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:03:16 2022

@author: Ivar
https://open.kattis.com/problems/divvyingup
"""


N = int(input())

summ = sum([int(i) for i in input().split()])

if summ % 3 != 0:
    print('no')
else:
    print('yes')