#Primeira e última ocorrência

frase = str(input("Escreva uma frase qualquer: "))
frase = frase.lower()
conta = frase.count('a')
print("Aparece {} vezes a letra 'a'" .format(conta))
posicao = frase.find('a') + 1
print("Aparece a letra 'a' pela primeira vez na posição {}" .format(posicao))
ultima = frase.rfind('a') + 1
print("Aparece a letra 'a' pela ultima vez na posição {}" .format(ultima))
