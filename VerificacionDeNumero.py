# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 19:50:17 2021

@author: fiore
"""
#Función para ingresar un número
#Parámetro de entrada: No tiene
#Parámetro de salida: n, el cual es un número ingresado por el usuario de tipo entero
def ingresarnum():
    n = int(input("Ingrese número: "))
    return n

#Parte principal del programa
if __name__ == '__main__':
    
    #x, almacena el número ingresado por el usuario
    x = ingresarnum()
    
    #Condiciona en caso el número sea mayor que cero imprimirá que el número es positvo
    if x > 0:
        print("El número ingresado es positivo")
    #Si el número no es mayor, sino menor que cero, imprimirá que el número es negativo
    elif x < 0: 
        print("El número ingresado es negativo")
    #Si el número ingresado no cumple las características anteriores imprimirá que es nulo
    else:
        print("El número ingresado es nulo")
