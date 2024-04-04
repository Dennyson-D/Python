# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:47:38 2024

@author: denny
"""

#Calucladora IMC  - Indice de massa corporal



alt = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))

imc = peso/alt**2

if imc < 18.5:
   print('Magreza')

elif imc >= 18.5 and imc < 24.9:
   resp =  'Normal'
elif imc >= 25 and imc < 29.9:
   resp = 'sobrepeso'
elif imc >= 30 and imc < 39.9:
   resp = 'Obesidade'
else:
    resp = 'Obesidade grave'   
         
print(f' Seu imc é {imc}, {resp}')