"""Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1"""

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)

valor = int(input('Digite o valor que você quer sacar: R$ '))
cedula50 = cedula20 = cedula10 = cedula1 = 0
while valor > 0:
    if valor >= 50:
        valor -= 50
        cedula50 += 1
    elif 20 <= valor < 50:
        valor -= 20
        cedula20 += 1
    elif 10 <= valor < 20:
        valor -= 10
        cedula10 += 1
    else:
        valor -= 1
        cedula1 += 1
if cedula50:
    print(f'Foram entregues {cedula50} nota(s) de R$ 50.00')
if cedula20:
    print(f'Foram entregues {cedula20} nota(s) de R$ 20.00')
if cedula10:
    print(f'Foram entregues {cedula10} nota(s) de R$ 10.00')
if cedula1:
    print(f'Foram entregues {cedula1} nota(s) de R$ 1.00')
