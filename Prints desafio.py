# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 22:08:11 2024

@author: denny
"""
primeiro_nome = input('Digite nome: ')
idade = input('Idade: ')

#forma 1
print('primeiro nome  {}, idade {}' .format(primeiro_nome,idade))

#forma2
print('primeiro nome', primeiro_nome, 'idade', idade)


#forma 3
print(f'primeiro nome {primeiro_nome} idade ,{idade}')