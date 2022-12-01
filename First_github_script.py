# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 13:37:10 2022

@author: James
"""
import random
n = random .randrange(1,10)
guess = int(input("Enter any number:"))
while n!= guess:
    if guess < n:
        print("Too Low")
        guess = int(input("Enter any number:"))
    elif  guess > n:
       print("Too High") 
       guess = int(input("Enter number again: "))
    else:
     break 
print("You guessed it right!!") 