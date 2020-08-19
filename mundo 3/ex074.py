from random import randint
tupla_sortida = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print("Os valores sortiados são: ", end='')
for n in tupla_sortida:
    print(f'{n}', end=' ')
organizar = sorted(tupla_sortida)
maior = organizar[4]
menor = organizar[0]
print(f"\nO maior número é {maior}")
print(f"O menor número é {menor}")