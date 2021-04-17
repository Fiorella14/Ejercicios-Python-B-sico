# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 10:40:26 2021

@author: fiore
"""

#función para ingresar un número
#Parametro de entrada: no tiene
#Parametro de salida: numinicial, es un número que ingresa el usuario tipo float
def ingresenum():
    numinicial = float(input("ingrese un número: "))
    return numinicial

#función para realizar el cálculo
#Parametro de entrada: n, es un número ingresado por el usuario tipo float
#Parámetro de salida: calc, es el cálculo solicitado
def calculo(n):
    calc = n+n*n+n*n*n
    return calc

#Programa principal
if __name__ == '__main__':
    # x almacena el número ingresado por el usuario llamando a la función ingresenum
    x = ingresenum()
 
    # calc, realiza el cálculo solicitado llamando a la función calculo ingresando como parámetro
    # el valor de x
    calc = calculo(x)
    print(calc)