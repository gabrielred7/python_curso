#Tabuada v.2

t = int(input("Digite um numero para fazer a tabuada do mesmo: "))
for v in range(0, 11):
    r = int(t * v)
    print("{} x {} = {}".format(t, v, r))