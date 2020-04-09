#Primeiro e último nome

nome = str(input("Digite um nome completo: "))
nome = nome.split()
primeiro = nome[0]
ultimo = nome[len(nome)-1]
print('Seu primeiro nome é: {}' .format(primeiro))
print('Seu ultimo nome é: {}' .format(ultimo))

