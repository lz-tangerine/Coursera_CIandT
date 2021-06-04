""" Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
– O primeiro valor é mair ; – O segundo valor é maior; – Não existe valor maior, os dois são iguais """

num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
maior = num1 if num1 > num2 else num2
if num1 == num2:
    print('Os dois valores são iguais')
elif maior == num1:
    print('O PRIMEIRO valor é maior')
elif maior == num2:
    print('O SEGUNDO valor é maior')




