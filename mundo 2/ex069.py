#Analise de dados do grupo
maiores = homens = mulheres = 0
while True:
    print("=" * 20)
    print("Cadastre uma Pessoa")
    print("=" * 20)
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in 'MmFf':
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    print("=" * 20)
    continua = " "
    while continua not in 'SsNn':
        continua = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if idade > 18:
        maiores = maiores + 1
    if sexo in "Mm":
        homens = homens + 1
    if sexo in "Ff" and idade < 20:
        mulheres = mulheres + 1
    if continua[0] in "Nn":
        break
print(f"Total de pessoas com mais de 18 anos: {maiores}")
print(f"Ao todo temos {homens} homens cadastrados")
print(f"E temos {mulheres} mulheres com menos de 20 anos")