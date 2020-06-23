#Jogo do par ou impar

from random import randint
print("="*20)
print("Vamos Jogar Par ou Impar")
print("="*20)
cont = 0
while True:
    pc = randint(0, 10)
    valor = int(input("Digite um valor: "))
    soma = valor + pc
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input("Par ou Impar? [P/I] ")).strip().upper()[0]
    print(f"Você jogou {valor} e o computador {pc}. Total de {soma}.")
    print("DEU PAR" if soma % 2 == 0 else "DEU IMPAR")
    if escolha in 'Pp':
        if soma % 2 == 0:
            print("Você Ganhou!")
            cont = cont + 1
        else:
            print("Você Perdeu!")
            break
    elif escolha in 'Ii':
        if soma % 2 != 0:
            print("Você Ganhou!")
            cont = cont + 1
        else:
            print("Você Perdeu!")
            break
    print("Vamos jogar de novo...")
    print("=-=" * 20)
print("=-=" * 20)
print(f"Game Over! Você venceu {cont} vezes.")