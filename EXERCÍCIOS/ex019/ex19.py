from random import choice
al_1 = input('Primeiro aluno: ')
al_2 = input('Segundo aluno: ')
al_3 = input('Terceiro aluno: ')
al_4 = input('Quarto aluno: ')
lista = [al_4, al_3, al_2, al_1]
escolhido = choice(lista)
print(f'Aluno escolhido: {escolhido}')
