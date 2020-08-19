lista = list()
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    continua = " "
    while continua not in 'SsNn':
        continua = str(input("Quer continuar? [S/N] "))
    if continua in "Nn":
        break
print("-="*30)
print(f"Você digitou {len(lista)} elementos.")
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são {lista}")
if 5 in lista:
    print("O valor 5 faz parte da lista.")
else:
    print("O valor 5 não consta na lista")
