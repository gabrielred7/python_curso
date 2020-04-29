#Gerenciador de Pagamentos

preço = float(input("Informa o preço normal do produto: "))
condicao = int(input("Escolha a forma de pagamento entre: "
                     "\n1- à vista dinheiro/cheque com 10% de desconto"
                     "\n2- á vista no cartão com 5% de desconto"
                     "\n3- em até 2x no cartão mas com preço normal"
                     "\n4- 3x ou mais no cartão com 20% de juros"
                     "\n:"))
if condicao == 1:
    desconto = (preço * 10)/100
    novo = preço - desconto
    print("À vista no dinheiro, você paga {}." .format(novo))
elif condicao == 2:
    desconto = (preço * 5) / 100
    novo = preço - desconto
    print("À vista no cartão, você paga {}." .format(novo))
elif condicao == 3:
    novo = preço / 2
    print("À vista no cartão, você paga {} a cada 2 meses.".format(novo))
elif condicao == 4:
    aumento = (preço * 20) / 100
    novo = preço + aumento
    parcela = novo / 3
    print("À vista no cartão, você paga {} a cada 3 meses.".format(parcela))
