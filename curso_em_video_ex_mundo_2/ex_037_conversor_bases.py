"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

numero = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão: \n'
      '[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    binario = bin(numero)
    print(f'O numero {numero} convertido para BINÁRIO é igual {binario[2:]}')
elif opcao == 2:
    octal = oct(numero)
    print(f'O numero {numero} convertido para OCTAL é igual {octal[2:]}')
else:
    hexa = hex(numero)
    print(f'O numero {numero} convertido para OCTAL é igual {hexa[2:]}')