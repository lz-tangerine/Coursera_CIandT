#Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.

valor = int(input('Digite um número inteiro: '))
dezena = valor // 10 % 10

print('O dígito das dezenas é {}'.format(dezena))
