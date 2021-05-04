# -*- coding: utf-8 -*-
"""
Created on Sat May  1 09:36:56 2021

@author: fiore
"""
hora_partida = float(input("Ingrese hora de partida: "))
hora_entrada = 8

if (hora_entrada - hora_partida) >= 1: 
    print("llegaré a tiempo, puedo ir en bus")
elif  (hora_entrada - hora_partida >= 0.5):
    print("llegaré a tiempo si voy en taxi")
else:
    print("Llegaré tarde")
