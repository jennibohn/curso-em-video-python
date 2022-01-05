dias = int(input('Quantidade de dias alugado: '))
km = float(input('Quantidade de km percorridos: '))
preçokm = km * 0.15
preçodias = dias * 60.00
total = preçokm + preçodias

print('O total a pagar é de R${:.2f}'.format(total))