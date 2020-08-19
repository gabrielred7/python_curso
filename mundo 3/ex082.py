par = list()
impar = list()
lista = list()
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    continua = " "
    while continua not in 'SsNn':
        continua = str(input("Quer continuar? [S/N] "))
    if continua in "Nn":
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print("-="*30)
print(f"A Lista completa é: {lista} ")
print(f'A lista de pares é {par}')
print(f"A lista de impares é {impar}")
