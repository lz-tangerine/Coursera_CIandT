'''Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros
correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir,
usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo
informado com caracteres '#' na saída.'''

largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
y = 1
while y <= altura:
    x = 1
    while x <= largura:
        if x == 1 or x == largura or y == 1 or y == altura:
            print('#', end='')
        else:
            print(' ', end='')
        x += 1
    y += 1
    print()
