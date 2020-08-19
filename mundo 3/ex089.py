#Boletim com listas compostas

dado = list()
alunos = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    alunos.append([nome, [nota1, nota2], media])
    continua = " "
    while continua not in "SsNn":
        continua = str(input("Quer continua? [S/N] "))
    if continua in "Nn":
        break
print('-='*20)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-='*20)
for i, j in enumerate(alunos):
    print(f'{i:<4}{j[0]:<10}{j[2]:8.1f}')
while True:
    print('-='*20)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(alunos) - 1:
        print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
print('<<< Volte Sempre >>>')