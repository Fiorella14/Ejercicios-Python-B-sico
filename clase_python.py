# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import sys

def main(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python %s celcius_degree' % sys.argv[0])
    else:
        celsius = float(sys.argv[1])
        fahrenheit = main(celsius)

        print(
            '%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %
            (celsius, fahrenheit))
