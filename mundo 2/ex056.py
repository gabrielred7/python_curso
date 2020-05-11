#Analisador completo
soma_idade = 0
media_idade = 0
tot_mulher20 = 0
maioridade_homem = 0
nome_velho = str("")

for p in range(1, 5):
    print("----- {}ª PESSOA -----" .format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    soma_idade = soma_idade + idade
    if sexo in "Mm" and p == 1:
        maioridade_homem = idade
        nome_velho = nome
    if sexo in "Mm" and idade > maioridade_homem:
        maioridade_homem = idade
        nome_velho = nome
    if sexo in "Ff" and idade < 20:
        tot_mulher20 = tot_mulher20 + 1

media_idade = soma_idade / 4
print("A media de idade do grupo é de {} anos" .format(media_idade))
print("O homem mais velho tem {} anos e se chama {}" .format(maioridade_homem, nome_velho))
print("Ao todo tem {} mulheres com menos de 20 anos" .format(tot_mulher20))