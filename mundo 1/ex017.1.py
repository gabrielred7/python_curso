#calculo da hipotenusa
import math
print("Vamos calcular a hipotenusa")
catetooposto = float(input("Digite o cateto oposto: "))
catetoadjacente = float(input("Digite o cateto adjacente: "))
somacatetos = (math.pow(catetooposto, 2) + math.pow(catetoadjacente, 2))
hipotenusa = math.sqrt(somacatetos)
print("O valor da hipotenusa é: {:.2f}" .format(hipotenusa))

