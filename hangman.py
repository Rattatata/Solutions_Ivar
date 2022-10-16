# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:22:29 2022

@author: Ivar
https://open.kattis.com/problems/hangman
"""

word = list(input())

guess = input()

win = True
counter = 0

for char in guess:
    if char in word:
        word = [sign for sign in word if sign != char ]
    else:
        counter += 1
    
    if counter == 10:
        win = False
        break
    if len(word) == 0:
        break
        

if win == True:
    print('WIN')
    
else:
    print('LOSE')
    