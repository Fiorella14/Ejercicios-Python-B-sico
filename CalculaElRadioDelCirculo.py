# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 11:02:04 2021

@author: fiore
"""

#Función ingresarradio, que permite al usuario ingresar el radio del círculo
#Parametro de entrada: No tiene
#Parametro de salida: radio, es el radio del círculo ingresado por el usuario y es del tipo float
def ingresarradio():
    radio = float(input("Ingrese el radio del círculo: "))
    return radio

#Función areacirculo, que calcula el área del circulo a partir del radio ingresado
#Parametro de entrada: radio, es el radio del círculo de tipo float
#Parámetro de salida: area, que es el área del círculo, es de tipo float
def areacirculo(radio):
    area = 3.1416*radio**2
    return area

#Parte principal del programa
if __name__ == '__main__':
    #r almacena el valor ingresado por el usuario llamando a la función ingresarradio()
    r = ingresarradio()
    #area, en area se asigna el área del circulo, llamando a la función areacirculo(), y que tiene como parámetro de entrada r
    area = areacirculo(r)
    #Muestra en pantalla el área del círculo
    print("El área del círculo es: ", area)
    