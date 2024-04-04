# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:21:41 2024

@author: denny
"""

#lista = [1,2,3,4,5,6,7,8,9,10,22,33,55,66,77,79]
# ou
lista = list(range(1,11))

for x in lista:
    if (x % 2 == 0):
        print (f'o número {x} é par')
    else:
        print (f'o número {x} é impar')