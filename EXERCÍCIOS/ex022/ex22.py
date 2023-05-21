valor_mensal = float(input('valor mensal:'))
horas_diarias = int(input('horas diarias:'))
dias_trabalhados = int(input('dias trabalhados por mês: '))
horas_m = horas_diarias * dias_trabalhados
valor_hora = valor_mensal / horas_m
print(valor_hora)
