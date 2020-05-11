#Soma dos pares
soma = 0
for i in range(1, 7):
    num = int(input("Digite o valor {}: " .format(i)))
    if num % 2 == 0:
        soma = soma + num
print("A soma dos numeros pares acima é: {}" .format(soma))