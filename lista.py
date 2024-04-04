
cidades = ['RJ','SP','Teresina']

print (cidades[0])
print (cidades[-1]) # -1 é o último

cidades.append('Salvador') # para adicionar

print(cidades[-1])

cidades.remove('Salvador') #para  remover

print(cidades[-1])

cidades.insert(1,'amazonas') # insert para escolher a posição index que quer inserir

print(cidades)

cidades.pop(2) # para retirar por index
cidades.sort() # para deixar em ordem alfabética
print(cidades)