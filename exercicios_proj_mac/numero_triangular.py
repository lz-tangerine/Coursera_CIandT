n = int(input('Digite o valor de n: '))
i = 1
while i * (i + 1) * (i + 2) < n:
    i = i + 1

if i * (i+1) * (i+2) == n:
    print('{} é o produto {} x {} x {}'.format(n, i, i+1, i+2))
else:
    print('{} não é triangular'.format(n))
