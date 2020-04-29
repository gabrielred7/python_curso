#Comparando números

v1 = int(input("Qual o primeiro valor: "))
v2 = int(input("Qual o segundo valor: "))
if v1 > v2:
    print("{} é o maior número" .format(v1))
elif v2 > v1:
    print("{} é o maior número" .format(v2))
else:
    print("Não existe valor maior, os dois são iguais")