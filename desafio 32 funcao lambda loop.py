# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:30:15 2024

@author: denny
"""


lista = [1,2,3,4,5,6]

quad = lambda x:x**2

res = []
 
for i in lista:
     res.append(quad(i))
    
print(res)