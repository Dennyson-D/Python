# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:03:36 2024

@author: denny
"""

amigos1 = {'Marcos','Cris','Ana','Amanda','Zé'}
amigos2 = {'Cris','Adonis','José','Luiz','Ana'}

comp = amigos1.intersection(amigos2) # compara e tráz as iguais
dif = amigos1.difference(amigos2)
unir = amigos1.union(amigos2)

print(f'comparar iguais, {comp}')
print(f'Nomes diferentes, {dif}')
print(f'Unir sem duplicações, {unir}')
      