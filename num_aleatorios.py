import random

#random.seed(1)   -- exemplo para pegar sempre o memso número
numero = random.randint(0,10)
print(numero)

##### outra forma com choice

lista = [1,2,3,4,5,6,7,8,9,10]

numero = random.choice(lista)
print(numero)
