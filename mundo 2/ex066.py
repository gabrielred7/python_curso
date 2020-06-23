#Varios números com flag

s = n = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
    c = c + 1
#fstring
print(f'Foram digitados {c} números e a soma dos números digitado vale {s}. ')