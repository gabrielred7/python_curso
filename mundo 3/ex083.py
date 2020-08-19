#Validando expressões matemáticas

expre = str(input('Digite a expressão: '))
pilha = list()
for simbo in expre:
    if simbo == '(':
        pilha.append('(')
    elif simbo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print("Sua expressão está errada!")
