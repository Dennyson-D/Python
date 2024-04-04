# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 20:46:15 2024

@author: denny
"""

r = int(input('Qual rendimento da lata: '))
h = int(input('Altura: '))
l = int(input('Largura: '))

def calcula_tinta():
    area = h * l
    total = area / r
    print(f' Voce precisa de {total} latas de tinta')

calcula_tinta()              