'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:'''

frase = str(input('Digite uma frase: ')).strip().upper().split()
juntar = ''.join(frase)
inverso = juntar[::-1]
print(f'O inverso de {juntar} é {inverso}!')
if juntar == inverso:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo!')

# feito com for (de maneira muito complicada)
# inverso = ''
# for letra in range(len(juntar)-1, -1, -1):
#    inverso += juntar[letra]
# print(f'O inverso de {juntar} é {inverso}!')
# if juntar == inverso:
#    print('Temos um palíndromo')
# else:
#    print('A frase digitada não é um palíndromo!')'''
