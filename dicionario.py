# Dicionários
# Utiliza index de keys e values
        # key       value
aluno = {'nome':'Dennyson', 'idade':36, 'Nota':10, 'aprovação': True}

#print(aluno['nome']) # aparecer apenas o nome

#atualizar valor
# 1ª forma para 1 campo
aluno['nome'] = 'Vedita'
print(aluno)

#2ª forma - para vários campos ou add
aluno.update({'nome':'Dranzer', 'idade':27, 'Nota':7, 'Sobrenome':'Kadosh'})
print(aluno)

#verificar se existe e mostrar msg de erro customizada
#aluno.update({'identidade':444})
print(aluno.get('identidade','Não existe id'))

#remover item
del aluno['idade']
print(aluno)