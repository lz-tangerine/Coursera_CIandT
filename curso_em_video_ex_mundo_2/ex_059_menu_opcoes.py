"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar, [ 2 ] multiplicar
[ 3 ] maior, [ 4 ] novos números, [ 5 ] sair do programa, Seu programa deverá realizar a operação solicitada em cada caso."""
from time import sleep

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
sair = False
while not sair:
    sleep(0.5)
    opcoes = int(input('\nO que gostaria de fazer:\n'
                       '[ 1 ] SOMAR\n'
                       '[ 2 ] MULTIPLICAR\n'
                       '[ 3 ] MAIOR NUMERO\n'
                       '[ 4 ] DIGITAR NOVOS NÚMEROS\n'
                       '[ 5 ] SAIR DO PROGRAMA\n'
                       'Sua opção: '))
    if opcoes == 1:
        print('A soma desses dois valores é igual a {}!'.format(valor1 + valor2))
    elif opcoes == 2:
        print('A multiplicação desses dois valores é igual a {}!'.format(valor1*valor2))
    elif opcoes == 3:
        maior = valor1 if valor1 > valor2 else valor2
        print('O maior numero digitado foi {}!'.format(maior))
    elif opcoes == 4:
        valor1 = int(input('Digite o 1º novo valor: '))
        valor2 = int(input('Digite o 2º novo valor: '))
    elif opcoes == 5:
        sair = True
    else:
        print('Opção inválida! Tente novamente...')
print('Programa finalizado! Volte sempre')
