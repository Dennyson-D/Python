# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 23:12:25 2023

@author: denny
"""
''' FORMA PADRÃO

valores = []

for x in range(6):
    valores.append(x*10)
print (valores)    
'''

# LIST COMPREHENSION
valores = [x*10 for x in range(6)]

print(valores)