# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:58:14 2023

@author: denny
"""

try:
    letras = ['a','b','c']

    print(letras[3])
except IndexError:
    print('index inválido')