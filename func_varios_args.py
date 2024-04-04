# * faz com que possa digitar vários argumentos
def soma(*numero):

    resultado = 0

    for num in numero:
        resultado += num
    return resultado        

x = soma(1,2,3,4,5,6,7,8,9)

print(x)