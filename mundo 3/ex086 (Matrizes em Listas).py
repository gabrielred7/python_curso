#Matriz em Python

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lar in range(0, 3):
    for col in range(0, 3):
        matriz[lar][col] = input(f'Digite o valor de [{lar}, {col}]: ')
print('-='*30)
for lar in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lar][col]:^5}]', end='')
    print()