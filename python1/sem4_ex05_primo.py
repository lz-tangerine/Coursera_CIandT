'''Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo.
Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".'''

n: int = int(input('Digite um número inteiro: '))
i = 1
divisao = 0
while i <= n:
    if n % i == 0:
        divisao += 1
    i += 1
if divisao == 2:
    print('primo')
else:
    print('não primo')
