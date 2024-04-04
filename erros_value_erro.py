# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 22:14:53 2023

@author: denny
"""

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em numeros')
finally:  
    print('final')