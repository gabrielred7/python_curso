#Grupo da maioridade
from datetime import date
contmaior = 0
contmenor = 0
maioridade = str("")
data_atual = date.today().year
for c in range(1, 8):
    nasc = int(input("Digite o ano que a {}ª pessoa nasceu? " .format(c)))
    maior = data_atual - nasc
    if maior >= 21:
        contmaior = contmaior + 1
        maioridade = nasc
    else:
        contmenor = contmenor + 1
print("{} pessoas já atigiram a maioridade. Que são {}." .format(contmaior, maioridade))
print("{} pessoas não atingiram a maioridade penal. " .format(contmenor))