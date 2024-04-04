
# o argumento default sempre deve estar depois do non default
def func (nome,valor = 1):
    print(f'seu nome é {nome}')
    print(f'valor: {valor}')

func('den')