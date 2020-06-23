#Criando um menu de opções

resultado = float(0)
maior = float(0)
menor = float(0)
escolha = int(0)
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("O que você gostaria de fazer com esses números? ")
while escolha != 5:
    print("[1] somar\n"
          "[2] multiplicar\n"
          "[3] selecionar o maior\n"
          "[4] digitar novos números\n"
          "[5] sair do programar")
    escolha = int(input(">>>>>>> Informe sua escolha: "))
    if escolha == 1:
        resultado = n1 + n2
        print("O resultado de {} + {} é {}" .format(n1, n2, resultado))
    elif escolha == 2:
        resultado = n1 * n2
        print("O resultado de {} * {} é {}".format(n1, n2, resultado))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            menor = n2
        print("O maior valor é: {}".format(maior))
    elif escolha == 4:
        n1 = float(input("Digite o novo primeiro número: "))
        n2 = float(input("Digite o novo segundo número: "))
    print("=-=" *10)
print("Fim do programa")