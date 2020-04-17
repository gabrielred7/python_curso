#Aluguel do carro

print("Vamos calcular o valor do aluguel total do carro")
km = float(input("Qual foi a quantidade de quilometros percorridos pelo carro? "))
dias = int(input("Por quantos dias ele foi alugado? "))
valordias = 60*dias
valorkm = 0.15*km
total = valordias + valorkm
print("O aluguel do carro custou: {}" .format(total))
print("Valor total dos dias {}, valor total da quilometragem {}" .format(valordias, valorkm))
