#Pintando parede

largura = float(input('Diga a largura da parede em metros: '))
altura = float(input('Diga a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².' .format(largura, altura, area))
print('Para pintar essa parede, você precisará de {} l de tinta' .format(tinta))
