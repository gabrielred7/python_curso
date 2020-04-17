#Cálculo de desconto

prod = int(input("Qual é o preço do produto desejado? R$ "))
novo = prod - ((prod*5)/100)
print("O produto que custava R${:.2f} com a promoção de 5% passou custar R$ {:.2f}".format(prod, novo))

