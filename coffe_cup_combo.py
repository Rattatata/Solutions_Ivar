# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 15:22:56 2022

@author: Ivar
https://open.kattis.com/problems/coffeecupcombo
"""

N = int(input())


coffeindex = input()

counter = 0
coffees = 0


for idx in coffeindex:
    
    if idx == '0':
        coffees += -1
    else: 
        coffees = 3
    
    if coffees > 0:
        counter += 1
    
print(counter)
    
    
        
    
    