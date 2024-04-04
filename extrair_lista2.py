produtos =['carro','casa','avião','cerco',1,2,3,4]

# para incluir todos os itens conforme abaixo, 
# devem ter as mesmas qtdes de itens na lista e variaveis senão dará erro
#exemplo se quiser apenas os 4 primeiros itens
item1,item2,item3,item4,*outros = produtos

print(item1)
print(item2)
print(item3)
print(item4)
print(outros)