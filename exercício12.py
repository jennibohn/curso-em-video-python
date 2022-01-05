preco = float(input('Preço do produto: R$ '))
novo = preco - (preco * 5 / 100)
print('O preço atualizado do produto com desconto fica: R${:.2f}'.format(novo))