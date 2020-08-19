tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f"O número por extenso é '{tupla[num]}'")
    else:
        print("Tente de novo. ", end="")
    resp = str(input('Executar novamente? [S/N]: ')).upper().strip()[0]
    if resp in 'Nn':
        break
print('Programa finalizado.')