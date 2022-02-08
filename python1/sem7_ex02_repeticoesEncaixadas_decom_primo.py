def primo(numero):
    i = 1
    divisao = 0
    while i <= numero:
        if numero % i == 0:
            divisao += 1
        i += 1
    if divisao == 2:
        print('Este número é primo')
    else:
        print('Este numero não é primo')


n = int(input('Digite um numero inteiro > 1: '))
fator = 2
multiplicidade = 0
while n > 1:
    while n % fator == 0:
        multiplicidade += 1
        n = n / fator
    if multiplicidade > 0:
        print(f'Fator {fator} - Multiplicidade {multiplicidade}')
        primo(fator)
    fator += 1
    multiplicidade = 0

