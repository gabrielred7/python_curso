valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print('=-'*30)
print(f'Você digitou os valores {valores}')

print(f'O maior valor é {maior}, e ele está na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
# v é o valor e i é o indice no enumerate()
print(f'\nO menor valor é {menor}, e ele está na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
