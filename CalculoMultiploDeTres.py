# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 10:20:06 2021

@author: fiore
"""
#Tarea 4: Mostrar si un numero ingresado por el ususario es  multiplo de 3 o no

#Función para ingresar un número
#Parámetro de entrada: no tiene
#Parámetro de salida: numini, es un número ingresado por el usuario tipo integer
def ingresenum():
    numini = int(input("Ingrese número: "))
    return numini

#Funcion para realizar el calculo
#Parámetro de entrada: n, es el número ingresado por el usuario tipo entero
#Parámetro de salida: m, es el resultado de calcular el resto de dividir n entre 3
def multiplode3(n):
    m = n % 3
    return m

#Parte principal del programa
if __name__ == '__main__':
    #x, almacena el número ingresado por el usuario
    x = ingresenum()
    #y calcula el multiplo de 3     
    y = multiplode3(x)
    if y == 0:
        print("El número ingresado es múltiplo de 3 ")
    else:
        print(x, "no es múltiplo de 3")