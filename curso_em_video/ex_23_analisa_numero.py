numero = int(input('Informe um número: '))
print(f'Analisando o numero {numero}')
print(f'Unidade: {numero % 10 // 1}')
print(f'Dezena: {numero % 100 // 10}')
print(f'Centena: {numero % 1000 // 100}')
print(f'Milhar: {numero % 10000 // 1000}')
