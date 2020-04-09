#Conversor de Moeda

real = float(input("Quanto dinheiro você tem na carteira? R$ "))
dolar = real / 3.79
print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolar))
euro = real / 4.30
print("Com R${:.2f} você pode comprar e${:.2f}".format(real, euro))
iene = real / 0.034
print("Com R${:.2f} você pode comprar Y${:.2f}".format(real, iene))
