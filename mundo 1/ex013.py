#Calculo de reajuste salario

salario = float(input("Qual é o seu salário atual? "))
novo = salario + ((salario*15)/100)
print("Seu novo salário com aumento de 15% é: {:.2f}" .format(novo))