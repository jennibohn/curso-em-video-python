preco = float(input('Qual é o preço do produto? '))
desconto = 0.05
precoDesconto = preco * (1 - desconto)
print('O preço {} atualizado do produto com desconto fica {}'.format(preco, precoDesconto))