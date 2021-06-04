s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
triangulo = s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2
if triangulo:
    print('O segmento acima PODE formar um triangulo')
else:
    print('O segmento acima NÃO PODE formar um triangulo')


