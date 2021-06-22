'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

n = int(input('Digite um numero: '))
divisao = 0
for i in range(1, n+1):
    if n % i == 0:
        divisao += 1
        print(f'\033[31m{i}\033[m', end=' ')
    else:
        print(i, end=' ')
if divisao <= 2:
    print(f'\nEsse numero foi dividido somente 2x por isso ele É PRIMO!!')
else:
    print(f'\nEsse numero foi dividido {divisao}x por isso ele NÃO É PRIMO!!')




