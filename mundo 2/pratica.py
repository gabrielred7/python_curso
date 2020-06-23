'''
for c in range(1,10):
    print(c)
print("Fim")
'''

s = n = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print("A soma vale {}" .format(s))
#fstring
print(f'A soma vale {s} ')