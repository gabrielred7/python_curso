#Ano Bissexto

from datetime import date
print("Descubra se o ano foi bissexto")
ano = int(input("Digite o ano, ou coloque zero para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
    print("O ano atual é {}" .format(ano))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print("O ano é BISSEXTO")
else:
    print("Não é BISSEXTO")
