"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo."""
from random import randint

print('*'*30)
print('{:^30}'.format('VAMOS JOGAR PAR OU ÍMPAR!'))
print('*'*30)
print('')

contador = 0
while True:
    escolha_usuario = ' '
    while escolha_usuario not in 'PpIi':
        escolha_usuario = str(input('Par ou ímpar? [P/I]: ')).upper().strip()[0]
    num_usuario = int(input('Escolha seu valor entre 0 e 10: '))
    num_aleatorio = randint(0, 10)
    soma = num_usuario + num_aleatorio
    par = soma % 2 == 0

    if par:
        print('~' * 30)
        print(f'Você jogou {num_usuario} e o computador {num_aleatorio} e o total foi {soma}! DEU PAR!')
        if escolha_usuario == 'P':
            print('VOCÊ VENCEU!!')
            print('~' * 30)
            print('')
            contador += 1
        else:
            print('VOCÊ PERDEU!!')
            print('')
            break

    else:
        print('~' * 30)
        print(f'Você jogou {num_usuario} e o computador {num_aleatorio} e o total foi {soma}! DEU ÍMPAR')
        if escolha_usuario == 'I':
            print('VOCÊ VENCEU!!')
            print('~' * 30)
            print('')
            contador += 1
        else:
            print('VOCÊ PERDEU!!')
            print('')
            break
    print('Vamos jogar de novo... ')

print('*'*30)
print(f'GAME OVER!! VOCÊ VENCEU {contador}x!')
print('*'*30)
