"""Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado: EQUILÁTERO: todos os lados iguais, ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

triangulo = s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2

if triangulo:
    print('O segmento acima PODE formar um triangulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO!')
    else:
        print('ISOSCELES')
else:
    print('O segmento NÃO PODE formar uma reta!')

"""equilatero = s1 == s2 == s3
isosceles = s1 == s2 and s1 != s3 or s1 == s3 and s1 != s2 or s2 == s3 and s2 != s1
escaleno = s1 != s2 != s3 != s1"""
