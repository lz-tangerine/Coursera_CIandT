'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
maior = 0
menor = 0
ano_atual = date.today().year
for i in range(1, 8):
    nasc = int(input(f'Em que ano a {i}º pessoa nasceu? '))
    maioridade = ano_atual - nasc
    if maioridade <= 21:
        menor += 1
    else:
        maior += 1
print('')
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E tambem tivemos {menor} pessoas menores de idade')
