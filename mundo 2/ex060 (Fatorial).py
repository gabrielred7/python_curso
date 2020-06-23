#Calculo do fatorial
fatorial = 1
numero = int(input("Digite o número para calcular o fatorial: "))
i = numero
while i >= 1:
    fatorial = fatorial * i
    i = i - 1
print("O fatorial de {} é {}." .format(numero, fatorial))
