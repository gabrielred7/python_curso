#Radar Eletrônico

print("Vamos brincar de radar")
vel = int(input("Diga a velocidade do carro: "))
if vel > 80:
    print("Voce foi multado pois o limite é 80km, seu miliante")
    limite = vel - 80
    multa = limite * 7.00
    print("A multa é de R${}" .format(multa))
else:
    print("Você não foi multado. Respeitou o limite")