#Alistamento militar

from datetime import date
data_atual = date.today().year
ano = int(input("Informe seu ano de nascimento: "))
idade = data_atual - ano
print(idade)
if idade < 18:
    tempo = 18 - idade
    print("Falta ainda {} anos para você se alistar. Ta ferrado!" .format(tempo))
elif idade == 18:
    print("Está na hora de se alista. Boa sorte!")
else:
    tempo = idade - 18
    print("Já passou do tempo de alistamento á {} anos. " .format(tempo))