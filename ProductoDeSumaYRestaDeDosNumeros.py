# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 11:07:14 2021

@author: fiore
"""

#Función para ingresar un número
#Parámetro de entrada:No tiene
#Parámetro de salida: a, b, son números ingresados por el usuario los cuales son de tipo entero
def Ingresenum():
    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))
    return a, b

#Producto para realizar el producto de la suma y resta de dos números
#Parámetro de entrada: a y b, los cuales son numeros ingresados por el usuario de tipo entero
#Parámetro de salida: p, el cual es el resultado de multiplicar la suma y resta de los números ingresados por el usuario
def Producto(a, b):
    p = (a-b)*(a+b)
    return p
    
#Parte principal del programa
if __name__ == '__main__':
    #almacena los números a y b ingresados por el usuario
    a, b = Ingresenum()
    #p, calcula el producto de la suma y de la resta de los números ingresados
    p = Producto(a, b)
    print("El producto de (a+b)*(a-b) es: ", p)