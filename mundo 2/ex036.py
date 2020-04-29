#Aprovando Empréstimos

valor_casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o salario do aplicante? R$"))
anos = float(input("Quantos anos você pretende pagar? R$"))
prestacao = valor_casa / (anos * 12)
print("Para pagar uma casa de r${:.2f} em {} anos a prestação será de R${:.2f}" .format(valor_casa, anos, prestacao))
minimo = (salario * 30) / 100
print("Para pagar uma casa de {} o minimo do salario tem que ser {}" .format(prestacao, minimo))
if prestacao <= minimo:
    print("Emprestimo concedido")
else:
    print("Emprestimo NEGADO")