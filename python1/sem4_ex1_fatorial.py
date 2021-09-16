'''n = int(input('Digite o valor de n: '))
c = n
f = 1
while c > 0:
    f *= c
    c -= 1
print(f)'''


def fatorial(v):
    if v < 0:
        return 0
    r = 1
    for c in range(1, v + 1):
        r *= c
    return r

def test_fatorial():
    assert fatorial(0) == 1

def test_fatorial1():
    assert fatorial(1) == 1

def test_fatorial_negativo():
    assert fatorial(-10) == 0

def test_fatorial4():
    assert fatorial(4) == 24

def test_fatorial5():
    assert fatorial(5) == 120