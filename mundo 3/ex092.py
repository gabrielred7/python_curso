#Cadastro de Trabalhador em Python
from datetime import datetime
carteira = dict()
carteira['nome'] = str(input("Nome: "))
nasc = int(input("Ano de Nascimento: "))
carteira['idade'] = datetime.now().year - nasc
carteira['ctps'] = int(input("Carteira de Trabalho (0 não tem): "))
if carteira['ctps'] != 0:
    carteira['contratacao'] = int(input("Ano de Contratação: "))
    carteira['salario'] = float(input("Salário: R$"))
    carteira['aposentadoria'] = ((carteira['contratacao'] + 35) - datetime.now().year)
print("-="*20)
for k, j in carteira.items():
    print(f' - {k} tem o valor de {j}')