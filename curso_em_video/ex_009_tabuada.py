numero = int(input('Digite um numero para ver sua tabuada: '))
print('')
i = 0
while i < 10:
    i += 1
    print(f'{numero} x {i:2} = {numero * i:2}')
