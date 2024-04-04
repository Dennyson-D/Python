# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:04:16 2024

@author: denny
"""

pc = {
      'Brasil':'Brasilia',
      'Japão':'Tokio',
      'Portugal':'Liboas',
      'Israel':'Jerusalem',
      'Grecia':'Atenas'
      }

x = input('Digite país: ')

if x in pc:
    print(f'A capital do {x} é {pc[x]}')
else:
    print('Não tem') 