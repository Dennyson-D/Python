# diferença entre tuple e list, 
# tuple é imutavel e usa () ao invés de []

cores_list = ['azul','verde','vermelho']
cores_tuple = ('azul','verde','vermelho')

print(type(cores_list))
print(type(cores_tuple))


cores_list.append('branco')
#cores_tuple.append('branco') não funciona por ser tupla

print(cores_list)
print(cores_tuple)