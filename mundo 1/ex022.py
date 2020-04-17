#Analisando um Texto

nome = str(input("Digite o nome completo de uma pessoa: "))
maiuscula = nome.upper()
print("O nome com as letras maiusculas é: {}" .format(maiuscula))
minuscula = nome.lower()
print("O nome com as letras minusculas é: {}" .format(minuscula))
letras = len(nome) - nome.count(' ')
print("O nome tem {} letras ao todos" .format(letras))
primeiro = nome.split()
conta_primeiro = len(primeiro[0])
print("O primeiro nome tem {} letras" .format(conta_primeiro))