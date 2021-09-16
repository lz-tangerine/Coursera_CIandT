'''def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4'''


def fatorial(k):
    '''(int) -> int

    Recebe um inteiro k e retorna o valor de k!

    Pre-condicao: supoe que k eh um numero inteiro nao negativo.
    '''

    k_fat = 1
    c = 1
    while c <= k:
        k_fat *= c
        c += 1
    return k_fat

def combinacao(m, n):
    '''(int, int) -> int
    Recebe dois inteiros m e n, e retorna o valor de m!/((m-n)! n!)
    '''

    return fatorial(m) / (fatorial(m - n) * fatorial(n))

# testes
print("Combinacao(4,2) =", combinacao(4,2))
print("Combinacao(5,2) =", combinacao(5,2))
print("Combinacao(10,4) =", combinacao(10,4))
