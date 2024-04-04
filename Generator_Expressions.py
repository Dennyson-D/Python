from sys import getsizeof

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:32:36 2023

@author: denny
"""

num = [x * 10 for x in range(10)]
print(type(num))
print(getsizeof(num))

print('--------------------------------')

num = (x * 10 for x in range(10))
print(type(num))
print(getsizeof(num))