#Primeiras letras de um texto

cidade = str(input("Digite o nome da cidade: "))
cidade = cidade.upper()
cidade = cidade.split()
print('A cidade tem "santo" no nome?')
print('SANTO' in cidade[0])
