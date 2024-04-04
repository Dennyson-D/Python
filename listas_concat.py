numeros = [2,3,4,5]
letras = ['a','b','c','d']

final = numeros * 4 # multiplica pelo número de vez que vai copiar para lista

print(final)

final = numeros + letras #incluir numero com letras

print(final)

#outra forma é utilziar extend para concatenar listas

numeros.extend(letras)
print(numeros)