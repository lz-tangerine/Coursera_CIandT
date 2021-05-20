quantidade = int(input('Digite a quantidade de numeros que serão digitados: '))
n = 0
t = 0
p = 0
i = 0
while t < quantidade:
    n = int(input('Digite um numero para a sequencia: '))
    t = t + 1
    if n != 0:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1

print('Nessa sequencia temos {} pares e {} impares'.format(p, i))
