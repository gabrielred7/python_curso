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
        if soma % 2 == 0 and escolha in 'Pp':
            print(f"Você jogou {valor} e o computador {pc}. Total de {soma} DEU PAR.")
            print("==" * 10)
            print("Você Ganhou!")
            print("Vamos jogar de novo...")
            print("==" * 10)
        elif soma % 2 != 0 and escolha in 'Ii':
            print(f"Você jogou {valor} e o computador {pc}. Total de {soma} DEU IMPAR")
            print("==" * 10)
            print("Você Ganhou!")
            print("Vamos jogar de novo...")
            print("==" * 10)
        elif soma % 2 == 0 and escolha in 'Ii':
            print(f"Você jogou {valor} e o computador {pc}. Total de {soma} DEU PAR.")
            print("==" * 10)
            print("Você Perdeu!")
            print("E o jogo acabou...")
            print("==" * 10)
            break
        elif soma % 2 != 0 and escolha in 'Pp':
            print(f"Você jogou {valor} e o computador {pc}. Total de {soma} DEU IMPAR")
            print("==" * 10)
            print("Você Perdeu!")
            print("E o jogo acabou...")
            print("==" * 10)
            break
        cont = cont + 1
print("=-=" * 20)
print(f"Game Over! Você venceu {cont} vezes.")