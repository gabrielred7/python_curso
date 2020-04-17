from math import hypot
print("Vamos calcular a hipotenusa")
catetooposto = float(input("Digite o cateto oposto: "))
catetoadjacente = float(input("Digite o cateto adjacente: "))
hipotenusa = hypot(catetooposto, catetoadjacente)
print("O valor da hipotenusa é: {:.2f}" .format(hipotenusa))
