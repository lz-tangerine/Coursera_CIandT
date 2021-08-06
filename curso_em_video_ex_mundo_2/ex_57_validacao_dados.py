'''Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

resposta = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while resposta not in 'MF':
    resposta = str(input('Dados inválidos. Por favor escolha entre [M]asculino ou [F]eminino: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(resposta))

