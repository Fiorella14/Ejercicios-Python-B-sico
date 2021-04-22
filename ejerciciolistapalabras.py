# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 23:22:36 2021

@author: fiore
"""


#Función para ingresar una lista
#Parámetro de entrada: No tiene
#Parámetro de salida: x, es la lista de palabras ingresadas por el usuario
def ingreselista():
    x = str(input("Ingrese lista de palabras: "))
    return x

if __name__ == '__main__':
    # f. almacena la lista ingresada por el usuario la cual es de tipo string
    f = ingreselista()
    print("******")
    print("*", f, end = "*")
    
    
