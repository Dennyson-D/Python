# similar a listas
# não mostra itens duplicados
# não usa index

lista1 = [10,20,30,40,50]
lista2 = [10,20,60,70]

num1= set(lista1)
num2 = set(lista2)

print(num1 | num2) # Union | unifica as 2 listas unificando os repetidos
print(num1 - num2) # Difference - mostra só valores unicos, tira repetidos
print(num1 ^ num2) # Symmetric difference - unifica as 2 listas retirando os repetidos
print(num1 & num2) # And - mostra só os repetidos