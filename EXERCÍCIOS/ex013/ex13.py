salario = float(input('Qual o salário mensal?'))
aumento = 0.15
aumento_em_reais = salario * aumento
salario_mais_aumento = salario + (salario * aumento)
print('O salário (R${:.2f}) + 15% (R${:.2f}) será {:.2f}'.format(salario, aumento_em_reais, salario_mais_aumento))
