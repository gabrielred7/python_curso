#Maior e menor valores

continua = str("S")
soma = cont = media = maior = menor = 0
while continua in "Ss":
    num = int(input("Digite um numero: "))
    soma = soma + num
    cont = cont + 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continua = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma / cont
print("Você digitou {} números é a média foi {}." .format(cont, media))
print("O maior valor foi {} e o menor valor foi {}" .format(maior, menor))