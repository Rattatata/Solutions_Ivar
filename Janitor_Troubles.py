# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 09:39:14 2022

@author: Ivar
"""
#https://open.kattis.com/problems/janitortroubles

import math as m


a, b, c, d = [int(i) for i in input().split()]


s = (a+b+c+d)/2

K = m.sqrt((s-a)*(s-b)*(s-c)*(s-d))

print(K)

