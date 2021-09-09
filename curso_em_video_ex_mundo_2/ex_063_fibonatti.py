"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci."""

num_anterior = 0
fibonatti = 1

termo = int(input('Digite a quantidade de termos a serem mostrador: '))
contador = 0
while contador < termo:
    num_anterior += fibonatti
    fibonatti = num_anterior - fibonatti
    print(fibonatti, end=' ')
    contador += 1
