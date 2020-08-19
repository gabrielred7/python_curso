##Mais sobre Matriz em Python

soma = valcol = maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lar in range(0, 3):
    for col in range(0, 3):
        matriz[lar][col] = int(input(f'Digite o valor de [{lar}, {col}]: '))
print('-=' * 30)
for lar in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lar][col]:^5}]', end='')
        if matriz[lar][col] % 2 == 0:
            soma = soma + matriz[lar][col]
    print()
print('-=' * 30)
print(f'soma dos valores pares é {soma}')
for lar in range(0, 3):
    valcol = valcol + matriz[lar][2]
print(f'A soma dos valores da terceira coluna é {valcol}')
for col in range(0, 3):
    if len(matriz) == 0:
        maior = matriz[1][col]
    else:
        if matriz[1][col] > maior:
            maior = matriz[1][col]
print(maior)