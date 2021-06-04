"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do
tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

ano_atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - nascimento
alistamento = 18

print('-'*40)

print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}!')
if idade < alistamento:
    print(f'Ainda faltam {alistamento - idade} anos para o alistamento!\n'
          f'Seu alistamento será em {ano_atual + (alistamento - idade)}!')
elif idade > alistamento:
    print(f'Você já deveria ter se alistado há {idade - alistamento} anos!\n'
          f'Seu alistamento foi em {ano_atual + (alistamento - idade)}!')
else:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
