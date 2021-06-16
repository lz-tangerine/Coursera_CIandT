"""Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50."""

for c in range(0, 50, 2): #nessa solução ele faz a metade da iteração comparado ao if
    print('.', end='') #mostra a quantidade de laços feitos sem imprimir nada
    print(c+2, end=' ')
