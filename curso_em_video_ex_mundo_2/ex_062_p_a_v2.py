primeiro_termo = int(input('Digite o primeiro termo: '))
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
print('Progressão finalizada com {} termos mostrados'.format(total))
