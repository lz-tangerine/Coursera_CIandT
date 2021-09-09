"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""

while True:
    numero = int(input('Digite o valor no qual quer ver a tabuada: '))
    print('-'*30)
    if numero < 0:
        break
    for c in range(1, 11):
        print(f'{numero} x {c:2} = {numero * c:2}')
    print('-' * 30)
print('PROGRAMA DE TABUADA ENCERRADO.')
