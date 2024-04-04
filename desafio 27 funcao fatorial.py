# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:32:01 2024

@author: denny
"""

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

x = int(input('Digite número:'))
print(f'Fatorial de {x} é {fatorial(x)}')    