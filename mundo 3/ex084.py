#Lista composta e análise de dados

pessoas = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    if len(pessoas) == 0: #Enquanto a lista principal não for preenchida ela continuara sendo 0
        maior = menor = dado[1] # Devido a isso o valor inicial de tudo sera o Peso do primeiro dados recebido
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:]) #Quando feito a analize enfim o dado 1 será enviado para a lista principal
    dado.clear() #Em seguida limpo para receber outro conjunto de dados para sofrer analise
    continua = " "
    while continua not in "SsNn":
        continua = str(input("Quer continuar? [S/N] "))
    if continua in "Nn":
        break
quant = len(pessoas)
print("=-"*30)
print(f'Ao todo você cadastrou {quant} pessoas.')

print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO maior peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')