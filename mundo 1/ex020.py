#Sorteando uma ordem

import random
n1 = str(input("Digite o Primeiro: "))
n2 = str(input("Digite o Segundo: "))
n3 = str(input("Digite o Terceiro: "))
n4 = str(input("Digite o Quarto: "))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(lista)
