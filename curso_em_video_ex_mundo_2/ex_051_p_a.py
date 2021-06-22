"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input(('Digite a razão: ')))
decimo = primeiro_termo + (11 - 1) * razao #calcula o décimo termo da PA
print(f'Os 10 primeiros termos são: ')
for n in range(primeiro_termo, decimo, razao):
    print(n, end=' → ')
print('Fim')
