#Sequência de Fibonacci v1.0
print("-" * 30)
print("Sequência de Fibonacci")
print("-" * 30)
# n = numero e p = posição
n1 = 0  #numero da posição1 é 0
n2 = 1  #numero da posição2 é 1
pn = int(input("Quantos termos(posições) você quer mostrar? "))
print('{} -> {}' .format(n1, n2), end='')
pi = 3  #começa nova posições a partir da posição3
while pi <= pn:  #Pecorre da posição3 até a posição escolhida
    n3 = n1 + n2  #Condição da prograssao ou razão
    print(' -> {}' .format(n3), end='')
    n1 = n2 #Reatribuição de valores
    n2 = n3
    pi = pi + 1
print(" -> FIM", end='')