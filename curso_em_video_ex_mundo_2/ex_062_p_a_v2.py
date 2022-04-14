"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará
quando ele disser que quer mostrar 0 termos. """

'''primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print('{}'.format(primeiro_termo), end=' → ')
        primeiro_termo += razao
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você quer mostrar: '))
print('Progressão finalizada com {} termos mostrados'.format(total))'''

contagem = 1
i = 1
while not i > 35:
    for letra in 'abcdef':
        print(f'{letra} = {contagem}', end=', ')
        contagem += 1
    i += 1
