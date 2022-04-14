"""Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 2
como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e,
se for o caso, n)."""

def n_primos(v):
    primo = 0
    i = 2
    while i <= v:
        div = 0
        c = 1
        while c <= v:
            if i % c == 0:
                div += 1
            c += 1
        if div <= 2:
            primo += 1
        i += 1
    return(primo)