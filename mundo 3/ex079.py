valor = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in valor:
        valor.append(n)
        print("Valor adicionado")
    else:
        print("Valor duplicado! Não adicionado")
    continua = " "
    while continua not in "SsNn":
        continua = str(input("Quer continuar? [S/N] "))
    if continua in "Nn":
        break
valor.sort()
print(f'Você digitou os valores {valor}')
