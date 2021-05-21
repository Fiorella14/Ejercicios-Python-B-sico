# -*- coding: utf-8 -*-
"""
Created on Tue May 18 00:28:10 2021

@author: fiore
"""

#adivina el numero secreto
numero_secreto = 777
n = int(input("Ingrese número secreto: "))
while n != numero_secreto:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    n = int(input("Ingrese número secreto: "))
print(n)
print("¡Bien hecho! Ahora eres libre.")