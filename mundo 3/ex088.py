#Palpites para a Mega Sena
from random import randint
from time import sleep
v = 0
lista = list()
jogos = list()
print('=-'*30)
print(f"{'JOGOS NA MEGA SENA':^10}")
print('=-'*30)
v = int(input("Quantos jogos você quer que eu sorteie? "))
for m in range(1, v+1): #For pra cada jogo
    for n in range(0, 7): #For para o numero de cada jogo
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print('-='*3, f' SORTEANDO {v} JOGOS ', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.7)
print('-='*5, '< BOA SORTE! >', '-='*3)