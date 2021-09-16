# funcao com while

'''def fatorial(n):
    fat = 1
    while (n > 1):
        fat *= n
        n -= 1
    return fat'''

#triangulo de pascal
def pascals_triangle(rows):
    answer = []
    for row in range(rows):
        answer.append(1)
        for i in range(row - 1, 0, -1):
            answer[i] += answer[i - 1]
        print(*answer)

def fatorial(x):
    r = 1
    for i in range(1, x + 1):
        r *= i
    return r

def num_binomial(n, p):
    return fatorial(n) // (fatorial(p) * fatorial(n - p))

print(pascals_triangle(10))





