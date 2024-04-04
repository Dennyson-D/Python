# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 14:13:59 2023

@author: denny
"""
x = int(input('Temperatura da carne: '))

if x < 48:
    print('precisa cozinhar mais')
elif x in range(48,53):
    print('Selado')
elif x in range(54,59):
    print('Ao ponto para mal')
elif x in range (60,64):
    print('Ao ponto') 
elif x in (65,70):
    print('Ao ponto par ao bem')
else:
    print('')    
    
    
 


 
 