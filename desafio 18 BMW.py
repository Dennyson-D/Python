# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 21:24:46 2024

@author: denny
"""

estoque = ['x6','i5','i8']

car = input('Digite o carro desejado: ')

if car in estoque:
    print('Disponivel')
else:
    print('Sem estoque')    