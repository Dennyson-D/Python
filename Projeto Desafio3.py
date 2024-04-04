# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:36:02 2024

@author: denny
"""

'''
Lista funcionários:
    lista1: funcs que tem carro e trabalham a noite
    lista2: funcs que tem carro e trabalham de dia
    lista3: funcs sem carro
'''        

funcionários =  ['Ana','Marcos','Alice','Pedro','Sophia','Bruno','Melissa']
turno_dia = ['Ana','Marcos','Alice','Melissa']
turno_noite = ['Pedro','Sophia','Bruno']
tem_carro = ['Marcos','Alice','Bruno','Melissa']

#listas

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)


lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

lista3 = set(funcionários).difference(tem_carro)
print(lista3)