def minima(temps):
    min = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min


def maxima(temps):
    max = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i += 1
    return max


def MinMax(temperaturas):
    print(f'A menor temperatura do mês foi {minima(temperaturas)} Cº')
    print(f'A menor temperatura do mês foi {maxima(temperaturas)} Cº')


MinMax([32, 22, 24, 30, 28, 27, 25, 33, 35, 18])
