# muito utilizado com listas
# aplicar uma função a um iterable, por item. (çlist, tuple, dic)

lista = [1,2,3,4]
'''
def mult(x):
    return x*2
'''

lista2 = map(lambda x: x*2,lista)

print(list(lista2)) # list para converter object map para lista