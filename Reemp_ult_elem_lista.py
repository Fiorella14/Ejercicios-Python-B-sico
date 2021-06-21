# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:49:30 2021

@author: fiore
"""

a = [1, 3, 5, 7, 9, 10]
b = [2, 4, 6, 8]

d=[]

for i in range(0, len(a)):
    if i < len(a)-1:
        d.append(a[i])
for l in range(0, len(b)):
    d.append(b[l])
print(d)
