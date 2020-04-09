#Jogo da Adivinhação

import random
from time import sleep
lista = [0, 1, 2, 3, 4, 5]
escolher = random.choice(lista)
print("Estou pensando em um numero. Consegue advinhar qual?")
jogador = int(input("I want play a game. Escolha um numero: "))
print("Processando...")
sleep(3)
if escolher == jogador:
    print("Venceu")
else:
    print("Perdeu. Eu pensei no numero {} e nao no {}. " .format(escolher, jogador))
