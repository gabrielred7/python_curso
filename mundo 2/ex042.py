#Analisando Triângulo 2.0

print("Descubra se de acordo com os lados estes possam se tornar um triângulo")
a = int(input("Digite lado 1: "))
b = int(input("Digite lado 2: "))
c = int(input("Digite lado 3: "))
if b-c < a < b+c and a-c < b < a+c and a-b < c < a+b:
    print("Isso pode resultar num triângulo")
    if a == b == c:
        print("O triangulo é equilátero")
    elif a != b != c:
        print("O triangulo é escaleno")
    else:
        print("O triangulo é isósceles")
else:
    print("Isso não pode resultar num triângulo")

