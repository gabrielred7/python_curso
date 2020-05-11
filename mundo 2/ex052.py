#Números primos
cont = 0
situ = ""
num = int(input("Digite um numero inteiro: "))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=" ")
        cont = cont + 1
        if cont == 2:
            situ = "\033[34mé primo"
        else:
            situ = "\033[31mnão é primo"
    else:
        print('\033[31m', end=" ")
    print("{}" .format(c), end=" ")
print('\n\033[30m O número {} foi divisível {} vezes então {}' .format(num, cont, situ), end='')
