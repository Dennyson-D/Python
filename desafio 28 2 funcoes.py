# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:50:47 2024

@author: denny
"""

def dobro(n1):
    return n1 * 2
    
def quad(n1):
    return dobro(n1)**2

x = int(input('Digite número: '))

print(f'O quadrado do dobro é: {quad(x)}')    