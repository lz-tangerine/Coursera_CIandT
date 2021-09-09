'''Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo.
Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".'''

n = int(input('Digite um número inteiro: '))
divisao = 0
c = 1
while c:
    if n % c == 0:
        divisao += 1
        c += 1
