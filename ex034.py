#Aumento Multiplo

print("Calculo do aumento do empregado")
print("Para salario acima de 1.250,00 é 10%, para inferior é 15%")
salario = float(input("Digite o valor do salario: "))
if salario >= 1250:
    aumento = salario + ((salario * 10)/100)
    print("O novo salario é R${}" .format(aumento))
else:
    aumento = salario + ((salario*15)/100)
    print("O novo salario é R${}" .format(aumento))
print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora." .format(salario, aumento))

res = 5 * 3 ** 2
print(res)