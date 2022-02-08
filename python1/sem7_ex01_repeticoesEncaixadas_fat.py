def fatorial(k):
    k_fat = 1
    c = 1
    while c <= k:
        k_fat *= c
        c += 1
    return k_fat


while True:
    valor_usuario = int(input('Digite o valor, ao final digite 0 para parar: '))
    while valor_usuario >= 0:
        print(f'O fatorial de {valor_usuario} é {fatorial(valor_usuario)}')
        break
    if valor_usuario < 0:
        break
