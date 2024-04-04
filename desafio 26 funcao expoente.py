# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:01:27 2024

@author: denny
"""

def expo(b,e=2):
    
    return b ** e
    
    
b=int(input('Digite base: '))
e=   (input('Digite exponente: '))

if e:
   print(f'O resultado é: {expo(b,int(e))}') 
else:
    print(f'Resultado: {expo(b)}')
