import math

x1 = float(input('Digite o primeiro numero: '))
x2 = float(input('Digite o segundo numero: '))
y1 = float(input('Digite o terceiro numero: '))
y2 = float(input('Digite o quarto numero: '))

d = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)

if math.sqrt(d) >= 10:
    print('longe')
else:
    print('perto')