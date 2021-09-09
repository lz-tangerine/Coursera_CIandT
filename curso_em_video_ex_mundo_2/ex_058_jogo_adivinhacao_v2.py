'''Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
from random import randint
print('Vou pensar em um numero de 1 a 10! Tente adivinhar...')
numero_escolhido = randint(1, 10)
escolha = int(input('Qual número eu pensei? '))
tentativa = 1
while escolha != numero_escolhido:
    if escolha < numero_escolhido:
        escolha = int(input('Mais... Tente novamente '))
    else:
        escolha = int(input('Menos... Tente novamente '))
    tentativa += 1

print('Você acertou na {}º tentativa'.format(tentativa))'''

from random import randint
print('Vou pensar em um numero de 1 a 10! Será que você consegue adivinhar...')
numero_escolhido = randint(1, 10)
tentativa = 1
acertou = False
while not acertou:
    escolha = int(input('Qual numero eu pensei? '))
    if escolha == numero_escolhido:
        acertou = True
    else:
        if escolha < numero_escolhido:
            print('Mais.... tente novamente!')
        elif escolha > numero_escolhido:
            print('Menos... tente novamente!')
        tentativa += 1
print('Acertou na {}º tentativa!'.format(tentativa))

