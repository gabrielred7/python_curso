#Jogo da adivinhação v2.0

from random import randint
tentativas = int(0)
acertou = bool(False)
escolher = randint(0, 10)
print("Estou pensando em um número de 0 a 10. Consegue advinhar qual?")
while not acertou:
    jogador = int(input("Escolha um número: "))
    if jogador == escolher:
        acertou = True
    else:
        if jogador < escolher:
            print("Mais! Tente de novo")
        elif jogador > escolher:
            print("Menos! Tente denovo")
    tentativas = tentativas + 1
print("Acertou! O número era {}. Mas você precisou de {} tentativas." .format(escolher, tentativas))
