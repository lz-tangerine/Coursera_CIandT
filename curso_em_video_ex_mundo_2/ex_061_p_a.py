"""Lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while."""

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
while cont < 10:
    print('{}'.format(primeiro_termo), end=' → ')
    primeiro_termo += razao
    cont += 1
print('Fim')

