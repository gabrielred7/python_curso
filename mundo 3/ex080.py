valores = list()
for cont in range(0, 5):
    n = int(input(f'Digite um valor: '))
    #Se for o 1º numero e se o numero for maior que o ultimo elemento, entao adicionar
    if cont == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista.')
    else:
        posição = 0
        while posição < len(valores):
            if n <= valores[posição]:
                valores.insert(posição, n)
                print(f'Adicionado na posição {posição} da lista...')
                break
            posição = posição + 1
print(f"Os valores digitados em ordem são: {valores}.")