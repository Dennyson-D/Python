from functools import reduce

def soma(x,y):
	return x-y

lista = [1,3,5,10,20]

somando = reduce(soma,lista)
print(somando) 	