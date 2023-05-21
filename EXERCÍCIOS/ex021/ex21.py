horas = float(input('Quantas horas trabalhadas: '))
mensal = float(input('Salário mensal: '))
valor_hora = mensal / horas
imposto = mensal * 0.11
inss = mensal * 0.08
sindicato = mensal * 0.05
liquido = mensal - (imposto + inss + sindicato)
print(f'Salário bruto: {mensal}\nValor/hora = {valor_hora}\nImposto = {imposto}\nINSS = {inss :.2f}\nSindicato = {sindicato}')
print(f'Salário liquido = {liquido}')
