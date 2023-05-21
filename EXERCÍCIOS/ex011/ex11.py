altura = float(input('Qual a altura da parede?'))
largura = float(input('Qual a largura da parede?'))
m2 = largura * altura
l2 = m2 / 2
print('{:.2f}m² precisará de {:.2f}L de tinta'.format(m2, l2))
