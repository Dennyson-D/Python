# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:34:57 2024

@author: denny
"""

frutas = ['maça','uva','maça','maça','kiwi']
cont = 0

for x in frutas:
    if x == 'maça':
       cont += 1
print('Contador =', cont)   

# alternativa
#print(frutas.count('maça'))
