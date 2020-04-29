#Game: Pedra, papel e tesoura
from random import randint
from time import sleep
print("Vamos jogar JOKENPO!")
print("Suas opções:"
      "\n [0] PEDRA"
      "\n [1] PAPEL"
      "\n [2] TESOURO")
itens = ("Pedra", "Papel", "Tesoura")
comp = itens[randint(0, 2)]
jogador = int(input("Escolha sua opção: "))
jogador = itens[jogador]
print("-=-"*7)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")
print("-=-"*7)
print("O Computador Jogou {}" .format(comp))
print("O Jogador jogou {}" .format(jogador))
print("-=-"*7)
if comp == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("O JOGADOR GANHOU")
    elif jogador == 2:
        print("O COMPUTADOR GANHOU")
    else:
        print("JOGADA INVALIDA")
elif comp == 1:
    if jogador == 0:
        print("O COMPUTADOR GANHOU")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("O JOGADOR GANHOU")
    else:
        print("JOGADA INVALIDA")
elif comp == 2:
    if jogador == 0:
        print("O JOGADOR GANHOU")
    elif jogador == 1:
        print("O COMPUTADOR GANHOU")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVALIDA")
print("-=-"*7)
