lista1 = [1,2,3,4,5]
lista2 = ['a','b','c','d','e']
lista3 = ['a1','a2','a3','a4','a5']
# usar zip para concatenar as 2 listas

for ind,valor,desc in zip(lista1,lista2,lista3):
	print(ind,valor,desc)