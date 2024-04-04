# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:59:32 2024

@author: denny
"""


''' -- função padrão
    def cubo(n):
    return n**3
'''

# Lambda

cubo = lambda n:n**3

x = int(input('Digite número:'))

print(f'o cubo de {x} é {cubo(x)}')
    