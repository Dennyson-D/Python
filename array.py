from array import array

# similar a lista
# melhor performance, usar quando a lsit for muito grande

letras = ['a','b','c','d','e']
num_i = [1,2,3,4,5]
num_f = [1.2,2.2,3.2,4.2,5.2]

print(letras)
print(num_i)
print(num_f)

letras = array('u',letras) # u, é o tipo de char
num_i = array('i',num_i) # i, é o tipo int
num_f = array('f',num_f) # f, é o tipo float

print(letras)
print(num_i)
print(num_f)
