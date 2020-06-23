#Progressão aritmética v2.0

print("Vamos calcular 10 primeiros termos de uma PA")
print("-=" * 10)
a1 = int(input("Digite o Primeiro Termo: "))
r = int(input("Digite a Razão da PA: "))
n = 1
while n <= 10:
    an = a1 + (n - 1) * r
    print("{} -> " .format(an), end=' ')
    n = n + 1
print("Fim", end=' ')
