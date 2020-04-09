#Analisando Triângulos

print("Descubra se de acordo com lados estes possam se tornar um triângulo")
a = int(input("Digite lado 1: "))
b = int(input("Digite lado 2: "))
c = int(input("Digite lado 3: "))
if b-c < a < b+c and a-c < b < a+c and a-b < c < a+b:
    print("Isso pode resultar num triângulo")
else:
    print("Isso não é um triângulo")