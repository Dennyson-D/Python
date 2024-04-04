# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:26:41 2024

@author: denny
"""
# até o 5
for x in range(1,11):
    if x > 5:
        break
    print(x)
    
# pular o 5    
for x in range(1,11):
    if x == 5:
        continue
    print(x)