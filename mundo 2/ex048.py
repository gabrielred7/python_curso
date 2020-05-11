#Soma impares múltiplos de três

c = input("Aperte enter para listar soma entre todos os números impar entre 1 a 500: ")
#Cria um acumulador
soma = 0
conta = 0
#Mostra os numeros impares
for n in range(1, 501, 2):
#Seleciona apenas os multiploes de três
    if n % 3 == 0:
        print(n, end=" ")
        soma = soma + n
        conta = conta + 1
print("\n")
print("A soma dos valores dos {} é: {}" .format(conta, soma))