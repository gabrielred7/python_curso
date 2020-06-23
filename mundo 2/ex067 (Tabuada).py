#Tabuada v3.0

print("Programa de Geração de Tabuadas")
print("-" * 10)
while True:
    cont = 0
    n = int(input("Digite um número: "))
    if n < 0:
        print("Programa Encerrado")
        break
    while cont <= 10:
        r = n * cont
        print(f"{n} * {cont} = {r}")
        cont = cont + 1
    print("-"*10)