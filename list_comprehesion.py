# Utilizado qdo precisar criar uma lista a partir de uma existente
# [Expressão for item in itens]

frutas1 = ['abacate','banana','morango','kiwi','abacaxi']

''' 
frutas2 =[]

for item in frutas1:
    if 'n' in item:
        frutas2.append(item)
'''
# fazer o c�digo comentado com list comprehesion
frutas2 = [item for item in frutas1 if 'n' in item]
print(frutas2)        