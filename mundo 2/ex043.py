#Ìndice de Massa Corporal

peso = float(input("Escreva o peso: "))
altura = float(input("Escreva a altura: "))
imc = peso/(altura * altura)
if imc < 18.5:
    print("IMC = {}" .format(imc))
    print("Você está abaixo do peso ideal")
elif imc >= 18.5 and imc < 25:
    print("IMC = {}" .format(imc))
    print("Você está no peso ideal")
elif imc >= 25 and imc < 30:
    print("IMC = {}" .format(imc))
    print("Você está com sobrepeso")
elif imc >= 30 and imc < 40:
    print("IMC = {}" .format(imc))
    print("Você está obeso")
else:
    print("IMC = {}" .format(imc))
    print("Você está com obesidade mórbida")
