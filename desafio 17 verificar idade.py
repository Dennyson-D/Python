# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 21:11:43 2024

@author: denny
"""

idade = int(input('Digite idade: '))

if idade < 13:
    print('Criança')
elif idade >= 13 and idade <= 19:
         print('Adolescente')
else:
    print('Adulto')
         