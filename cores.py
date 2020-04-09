print("\033[4;30;45mOlá, Mundo!")
print("\033[1;34;46mOlá, Mundo!\033[m")
print("\033[31mOlá, Mundo!")
print('\033[7;30mOla, Mundo!\033[m')
print('\033[0;33;44mOla, Mundo!\033[m')
print('\033[7;33;44mOla, Mundo!\033[m')

a = 3
b = 5
nome = "Gabriel"
print("Os valores são \033[32m{}\33[m e \033[31m{}\33[m!!!" .format(a, b))
print("Sou {}{}{}!!" .format('\033[4;34m', nome, '\033[m'))

cores = {'limpa':"\033[m",
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;30m'}
print("Sou {}{}{}!!" .format(cores['amarelo'], nome, cores['limpa']))

