#Seno, Cosseno e Tangente de um ângulo

import math
angulo = int(input("Digite um ângulo: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("Em um ângulo {}, o seno é {:.2f}, o cosseno é {:.2f} e a tangente {:.2f}." .format(angulo, seno, cosseno, tangente))
