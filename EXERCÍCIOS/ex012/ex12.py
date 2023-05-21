preco_produto = float(input('Digite o preço do produto: '))
desconto = 0.05
desconto_aplicado = preco_produto - (preco_produto * desconto)
print('{:.2f} Com o desconto de 5% será {:.2f}'.format(preco_produto, desconto_aplicado))