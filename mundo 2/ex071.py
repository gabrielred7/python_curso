#Simulador de caixa eletrônico
print("="*40)
print("{:^40}".format("BANCO MENDES"))
print("="*40)
valor = int(input("Que valor você quer sacar? R$"))
tot = valor
notas = 50
tot_notas = 0
while True:
    if tot >= notas:
        tot = tot - notas
        tot_notas = tot_notas + 1
    else:
        if tot_notas > 0:
            print(f"Total de {tot_notas} notas de R${notas}")
        if notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 1
        tot_notas = 0
        if tot == 0:
            break
print("=" * 40)
print("Volte sempre ao Banco Mendes! Tenha um bom dia")