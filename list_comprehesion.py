# Utilizado qdo precisar criar uma lista a partir de uma existente
# [ExpressÃ£o for item in itens]

frutas1 = ['abacate','banana','morango','kiwi','abacaxi']

''' 
frutas2 =[]

for item in frutas1:
    if 'n' in item:
        frutas2.append(item)
'''
# fazer o código comentado com list comprehesion
frutas2 = [item for item in frutas1 if 'n' in item]
print(frutas2)        