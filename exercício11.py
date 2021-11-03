largura = float(input('Qual é a largura? '))
altura =float(input('Qual é a altura? '))
area = largura * altura
tinta = 2
tintaNecessaria = area / tinta
print('A largura é {}, a altura é {} e a área é {}. A quantidade de tinta necessária para pintar a parede é {}l'.format(largura, altura, area, tintaNecessaria))