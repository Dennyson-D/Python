# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 19:42:51 2024

@author: denny
"""

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

# Exemplo de uso
resultado = fatorial(4)
print(resultado) 