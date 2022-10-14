# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:22:48 2022

@author: Ivar
https://open.kattis.com/problems/countthevowels
"""
string = input().replace(" ", "")

counter = 0
counters = ['A', 'E', 'I', 'O', 'U']
for letter in string:
    if letter.upper() in counters:
        counter += 1
print(counter)
        
