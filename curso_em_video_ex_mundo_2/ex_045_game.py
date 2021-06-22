"""Crie um programa que faça o computador jogar Jokenpô com você."""
from time import sleep
from random import randint

print('Suas opções: \n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL \n'
      '[ 2 ] TESOURA')
escolha_jogador = int(input('Qual é a sua jogada? '))
opcao = ('PEDRA', 'PAPEL', 'TESOURA')
print('-=-' * 15)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!')
print('-=-' * 15)
escolha_computador = randint(0, 2)
if escolha_computador == 0 and escolha_jogador == 1:
    print('Você GANHOU!! Computador escolheu PEDRA!')
elif escolha_computador == 1 and escolha_jogador == 2:
    print('Você GANHOU!! Computador escolheu PAPEL!')
elif escolha_computador == 2 and escolha_jogador == 0:
    print('Você GANHOU!! Computador escolheu TESOURA!')
elif escolha_computador == escolha_jogador:
    print('EMPATOU!! JOGUE NOVAMENTE!!')
else:
    print(f'PERDEU!! O Computador escolheu {opcao[escolha_computador]}')

