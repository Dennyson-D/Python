aluno = {'nome':'Dennyson', 'idade':36, 'Nota':10, 'aprovação': True}

# pegar a keys
for x in aluno:
    print(x)

#pegar values
for x in aluno.values():
    print(x)

#pegar itens inteiros em tuplas
for x in aluno.items():
    print(x)

#pegar valores separados
for k, v in aluno.items():
    print(k,v)