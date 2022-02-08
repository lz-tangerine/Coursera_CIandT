'''Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros
correspondentes à largura e à altura de um retângulo, respectivamente. O programa deve imprimir,
usando repetições encaixadas (laços aninhados), uma cadeia de caracteres que represente o retângulo
informado com caracteres '#' na saída.'''

largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))
a = 0
while altura > a:
    l = 0
    while largura > l:
        print('#', end='')
        l += 1
    a += 1
    print('')


