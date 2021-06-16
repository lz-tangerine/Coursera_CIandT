"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal
(IMC) e mostre seu status, de acordo com a tabela abaixo: IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""

peso = float(input('Digite seu peso kg: '))
altura = float(input('Digite sua altura: '))
IMC = peso / altura ** 2
if IMC:
    print(f'Seu IMC é de {IMC:.1f} você esta ', end='')
    if IMC <= 18.5:
        print('ABAIXO DO PESO IDEAL')
    elif 18.5 <= IMC < 25:
        print('no PESO IDEAL')
    elif 25 <= IMC < 30:
        print( 'ACIMA DO PESO IDEAL')
    elif 30 <= IMC < 40:
        print('MUITO ACIMA DO PESO IDEAL!')
    else:
        print('REALMENTE MUITO ACIMA DO PESO IDEAL')
else:
    print('Inválido, digite novamente um peso e uma altura!')
