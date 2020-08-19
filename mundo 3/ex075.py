numero = (int(input("Digite um número: ")),
          int(input("Digite outro número: ")),
          int(input("Digite mais número: ")),
          int(input("Digite o último número: ")))
print(f"Os números digitados são {numero}")
print(f"O valor 9 aparece {numero.count(9)} vezes")
if 3 in numero:
    print(f"O valor 3 apareceu {numero.index(3)+1}ª posição")
else:
    print("O 3 não consta em nenhum lugar")
print("Os valores pares digitados foram: ", end="")
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')