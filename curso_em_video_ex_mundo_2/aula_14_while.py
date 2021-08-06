'''for c in range(1, 10):
    print(c)
print('fim')

c = 1
while c < 10:
    print(c)
    c += 1
print('fim')

n = 1
while n != 0:
    n = int(input('Digite um numero: '))
print('Fim')

r = 'S'
quant = 0
soma = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    quant += 1
    soma += n
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Você digitou {} numeros e a soma deles foi {}'.format(quant, soma))'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} pares e {} impares'.format(par, impar))



