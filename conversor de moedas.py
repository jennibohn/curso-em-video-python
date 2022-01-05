real = float(input('Valor na carteira: '))
dolar = 3.27
euro = 6.41
iene = 0.049
print = float(input('O valor {} equivale à {:.2f} dólares, {:.2f} euros e {:.2f} ienes'.format(real, real / dolar, real / euro, real / iene)))