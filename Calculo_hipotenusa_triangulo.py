# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:28:50 2021

@author: fiore
"""


#print("My name is", "Python.", end="******")
#print("Monty Python.")

#print('Programming', 'essential','in', sep='***', end="...")
#print('Python')

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))