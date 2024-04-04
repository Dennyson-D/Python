# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:38:38 2024

@author: denny
"""

cidades = ('RJ','SP','SL')

cid = input('Advinhe nome da cidade: ')


if cid.upper() in cidades:
    print('certo!')
else:
    print ('errado')    
