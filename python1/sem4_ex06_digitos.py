"""Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao
menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não"."""
n = int(input('Digite um número inteiro: '))
anterior = n % 10
n = n // 10
adjacente = False
while n > 0 and not adjacente:
    atual = n % 10
    if atual == anterior:
        adjacente = True
    else:
        anterior = atual
        n = n // 10
if adjacente:
    print('sim')
else:
    print('não')
