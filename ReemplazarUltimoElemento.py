# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 23:25:32 2021

@author: fiore
"""

a = [1, 3, 5, 7, 9, 10]
b = [2, 4, 6, 8]

a.pop()
a.extend(b)
print(a)