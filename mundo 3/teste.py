pessoas = {'nome': 'Gabriel',
           'sexo': 'M',
           'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('---------------------')
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('---------------------')
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
    print('--------------------')
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()