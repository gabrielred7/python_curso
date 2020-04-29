#Conversor Numerico

num = int(input("Escolha um numero inteiro quaisquer: "))
base = int(input("Escolha um base de conversão entre: "
                 "\n[2] para binário "
                 "\n[8] para octal e "
                 "\n[16] para hexadecimal "
                 "\nSua opçao: "))
if base == 2:
    print("Em binário: {}" .format(bin(num)[2:]))
elif base == 8:
    print("Em octal: {}" .format(oct(num)[2:]))
elif base == 16:
    print("Em hexadecimal: {}" .format(hex(num)[2:]))
else:
    print("Base invalida")