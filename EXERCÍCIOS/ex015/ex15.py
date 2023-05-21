dias = int(input('Quantos dias alugado? '))
km_rodados = int(input('Quantos Km rodados? '))
pago = (dias * 60) + (km_rodados * 0.15)
print('O total a pagar é de R${}'.format(pago))
