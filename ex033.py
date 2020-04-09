#Maior e Menor

print("Descubra entre 3 numeros qual é o maior e o menor")
n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))
n3 = int(input("Terceiro numero: "))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print("O menor valor é: {}" .format(menor))

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print("O maior valor é: {}" .format(maior))
