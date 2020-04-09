nome = str(input('Qual é seu nome? '))
print('prazer em te conhecer {:=^20}!'.format(nome))
print('prazer em te conhecer {:^20}!'.format(nome))

n1 = int(input('manda valor: '))
n2 = int(input('manda valor: '))
print('A soma vale {}'.format(n1+n2))

s= n1 + n2
m= n1 * n2
d= n1 / n2
dI = n1 // n2
e = n1 ** n2

print('A soma é {}, e o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potencia {}'.format(dI, e))

