#Estatísticas em produtos

print("=" * 50)
print("LOJA SUPER BARATÃO")
print("=" * 50)
total = totmil = cont = 0
while True:
    prod = str(input("Nome do Produto: "))
    preço = float(input("Preço: R$"))
    continua = " "
    print("-" * 50)
    while continua not in 'SsNn':
        continua = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    print("=" * 50)
    if preço != 0:
        total = total + preço
    if preço > 1000:
        totmil = totmil + 1
    cont = cont + 1
    if cont == 1:
        menor = preço
        barato = prod
    else:
        if preço < menor:
            menor = preço
            barato = prod
    if continua in "Nn":
        break
print("{:-^40}" .format(' Fim do Programa '))
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {totmil} produtos custando mais de R$1000.00")
print(f"O produto mais barato é {barato} e custa R${menor:.2f}")