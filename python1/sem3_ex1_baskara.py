#Usando a modulo math, calcule a raiz quadrdada de delta, numa equação de segundo grau
#e imprima as raizes conforme o resultado

import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b ** 2) - (4 * a * c)
if delta < 0:
  print('Essa equação não possui raizes reais!')
else:
  x1 = (- b + math.sqrt(delta)) / (2 * a)
  x2 = (- b - math.sqrt(delta)) / (2 * a)

  if delta > 0:
    print('Essa equação possui duas raizes reais: {:.2f} e {:.2f}'.format(x1, x2))
  else:
    print('Essa equação possui uma raiz real que é {}!'.format(x1))