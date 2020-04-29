#Classificando atletas

from datetime import date
data_atual = date.today().year
nasc = int(input("Digite o anos de nascimento do atleta: "))
idade = data_atual - nasc
if idade <= 9:
    print("Sua categoria é MIRIM pois sua idade é {}." .format(idade))
elif idade > 9 and idade <= 14:
    print("Sua categoria é INFANTIL pois sua idade é {}." .format(idade))
elif idade > 14 and idade <= 19:
    print("Sua categoria é JUNIOR pois sua idade é {}." .format(idade))
elif idade > 19 and idade <= 25:
    print("Sua categoria é SÊNIOR pois sua idade é {}." .format(idade))
else:
    print("Sua categoria é MASTER pois sua idade é {}." .format(idade))