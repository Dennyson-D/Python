# ** significa que podem ter vários parametros

def agencia(**carro):
    return carro

print(agencia(modelo = 'prisma', cor = 'prata', motor = 1.4))