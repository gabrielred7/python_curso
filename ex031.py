#Custo de Viagem

viagem = float(input("Qual a distancia de sua viagem em quilometros: "))
if viagem < 200:
    custo = viagem * 0.50
    print("A sua viagem tem menos de 200km, estão sua viagem custa R${}. " . format(custo))
else:
    custo = viagem * 0.45
    print("A sua viagem tem mais de 200km, então sua viagem custa R${:.2f}." .format(custo))