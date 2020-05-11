#Contagem de pares

c = input("Aperte enter para lista numeros pares de 1 a 50: ")
for n in range(2, 51, 2):
    if n % 2 == 0:
        print(n, end=" ")