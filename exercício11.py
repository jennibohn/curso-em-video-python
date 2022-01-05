largura = float(input('Largura da parede: '))
altura =float(input('Altura da parede: '))
area = largura * altura
tinta = 2
tintaNecessaria = area / tinta
print('As dimensões da sua parede são {}x{} e a área é {}m². A quantidade de tinta necessária para pintar a parede é {}L'.format(largura, altura, area, tintaNecessaria))