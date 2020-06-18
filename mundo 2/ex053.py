#Detector de palíndromo

frase = str(input("Digite uma frase: "))
palavras = frase.strip().upper().split()
junto = ''.join(palavras)
inverso = str('')
for letras in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letras]
print("A frase é {} e seu inverso é {}." .format(junto, inverso))
if inverso == junto:
    print("É um palindromo")
else:
    print("Não é um palindromo")


