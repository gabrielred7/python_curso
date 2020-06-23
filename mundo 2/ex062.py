#Super progressão aritmetica v3.0

print("Vamos calcular 10 primeiros termos de uma PA")
print("-=" * 10)
a1 = int(input("Digite o Primeiro Termo: "))
r = int(input("Digite a Razão da PA: "))
n = 1
limite = 0
mais = 10
while mais != 0:
    limite = limite + mais
    while n <= limite:
        an = a1 + (n - 1) * r
        print("{} -> " .format(an), end=' ')
        n = n + 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print('FIM')