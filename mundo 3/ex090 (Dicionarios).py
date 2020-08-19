aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['media'] >= 7.0:
    aluno['situacao'] = str('Aprovado')
else:
    aluno['situacao'] = str('Reprovado')
print(f'Nome é igual: {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situacao"]}')
print(aluno)
