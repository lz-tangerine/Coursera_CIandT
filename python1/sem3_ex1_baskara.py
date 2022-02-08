"""Usando a modulo math, calcule a raiz quadrdada de delta, numa equação de segundo grau
#e imprima as raizes conforme o resultado

import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b ** 2) - (4 * a * c)
if delta < 0:
    print('esta equação não possui raízes reais!')
else:
    x1 = (- b + math.sqrt(delta)) / (2 * a)
    x2 = (- b - math.sqrt(delta)) / (2 * a)

    if delta > 0:
        if x1 < x2:
            print('as raízes da equação são {:.2f} e {:.2f}'.format(x1, x2))
        else:
            print('as raízes da equação são {:.2f} e {:.2f}'.format(x2, x1))
    else:
        print('a raiz desta equação é {}!'.format(x1))"""

import math


def delta(a, b, c):
    return (b ** 2) - (4 * a * c)


def main():
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    imprime_raizes(a, b, c)


def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        print('esta equação não possui raízes reais!')
    else:
        x1 = (- b + math.sqrt(d)) / (2 * a)
        x2 = (- b - math.sqrt(d)) / (2 * a)

        if d > 0:
            if x1 < x2:
                print('as raízes da equação são {:.2f} e {:.2f}'.format(x1, x2))
            else:
                print('as raízes da equação são {:.2f} e {:.2f}'.format(x2, x1))
        else:
            print('a raiz desta equação é {}!'.format(x1))

main()
