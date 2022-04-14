def maior_elemento(lista):
    maior = 0
    for n in lista:
        if n > maior:
            maior = n
        if maior < -n:
            maior = max(lista)
    return maior
