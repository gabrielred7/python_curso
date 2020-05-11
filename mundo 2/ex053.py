#Detector de palíndromo

frase = str(input("Digite uma frase: "))
frase = frase.strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letras in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letras]
print("A frase é {} e seu palindromo é {}." .format(junto, inverso))
if inverso == junto:
    print("É um palindromo")
else:
    print("Não é um palindromo")


