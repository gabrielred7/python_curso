#Analisando Variaveis

algo = input("Digite algo: ")
print("O tipo primitivo desse valor é", type(algo))
print("So tem espaço?", algo.isspace())
print('É um numero?', algo.isnumeric())
print('É alfabetico?', algo.isalpha())
print('É alfanumerico?', algo.isalnum())
print('Está em minusculas?', algo.islower())
print('Está em maiusculas?', algo.isupper())
print('Está capitalizado?', algo.capitalize())

#OBS: em algo.isqualquercoisa()
# algo é um objeto
# isqualquercoisa são metodos
