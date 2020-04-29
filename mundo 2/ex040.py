#Aquele clássico da Média

print("Vamos calcular a média")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2
if media < 5.0:
    print(media)
    print("Sua média está abaixo de 5.0. Você está REPROVADO.")
elif media >= 5.0 and media < 7:
    print(media)
    print("Sua média está entre 5.0 e 6.9. Você está de RECUPERAÇÃO.")
else:
    print(media)
    print("Sua média está acima de 7.0. Você está APROVADO.")