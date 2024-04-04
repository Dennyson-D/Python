# Filter
 # muito utilizado com lista
 # Aplicar uma função a um Iterables, filtrando itens. (list,tuple,dic etc)

valores = [10,12,34,55,77]

def remove20(x):
    return x > 20

print(list(filter(remove20, valores)))

# ou usando lambda e sem função

print(list(filter(lambda x: x>20,valores)))

