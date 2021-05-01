# -*- coding: utf-8 -*-
"""
Created on Sat May  1 08:49:55 2021

@author: fiore
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/fiore/Desktop/ML/Clase_5/data_sets/comprimido/train_triplets.txt", header = None, delimiter='\t', nrows=10000, names=['idUsuario','idCancion','play_count'])
plt.hist(df['idCancion'], edgecolor='black')
plt.title('Cantidad de Canciones Reproducidas')
plt.xlabel("Id de Canciones")
plt.ylabel("Número de Reproducciones")
plt.show()