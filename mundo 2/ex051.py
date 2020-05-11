#Progressão aritmética
print("Vamos calcular 10 primeiros termos de uma PA")
a1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
for n in range(1, 11):
    an = a1 + (n - 1) * r
    print("O valor do {} termo é {}" .format(n, an))