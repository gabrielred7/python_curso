palavras =('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
           'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
           'PRATICAR', 'TRABALHAR', 'MERCADO',
           'PROGRAMADOR', 'FUTURO')
for pas in palavras:
    print(f'\nNa palavra {pas} temos: ', end='')
    for letra in pas:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')