#Tratando vários valores v1.0

soma = cont = 0
num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    soma = soma + num
    cont = cont + 1
    num = int(input("Digite um número [999 para parar]: "))
print("Você digitou {} números e a soma entre eles é {}" .format(cont, soma))

