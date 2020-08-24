def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

def somalen(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

def contador(*num):
    for valor in num:
        print(f'{valor}', end=' ')
    print()
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')

def linha():
    print('-' * 15)

def mensagem(msg):
    print('=-' * 15)
    print(msg)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


mensagem('     SISTEMA DE ALUNOS     ')
mensagem('     APRENDA PYTHON        ')
mensagem('     GABRIEL ALMEIDA       ')
print('=-' * 15)

soma(b=4, a=5)
linha()
soma(7, 2)
linha()
soma(3, 9)

print('=-' * 15)

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 3)

print('=-' * 15)

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

print('=-' * 15)

somalen(5, 2)
somalen(2, 9, 4)