n = int(input('Digite um número inteiro: '))
soma = 0
while n > 0:
    div = n % 10
    soma += div
    n = n // 10
print(soma)
