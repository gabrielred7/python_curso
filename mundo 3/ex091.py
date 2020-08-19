from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print("Valores sorteados: ")
for i, v in jogo.items():
    print(f'{i} tirou {v} no dado.')
    sleep(1)
print('=-'*20)
print(f'{"== ":<2}{"RANKING DOS JOGADORES":^10}{" ==":>2}')
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
sleep(1)
for i, v in enumerate(rank):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}")
    sleep(1)