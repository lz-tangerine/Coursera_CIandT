"""Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que
se encontram no intervalo de 1 até 500."""
soma = 0
cont = 0
for c in range(3, 501, 6):
    soma += c
    cont += 1
print(f'A soma de todos os {cont} valores, multiplos de 3 no intervalo de 1 a 500, é {soma}')
