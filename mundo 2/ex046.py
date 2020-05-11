#Contagem Regressiva
from time import sleep
c = input("Aperte enter para a contagem regressiva: ")
for v in range(10, -1, -1):
    print(v, end=" ")
    sleep(1)
print("Estoura os fogos!!!")