"""Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
(desconsiderando o flag)."""

soma = cont = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor == 999:
        break
    cont += 1
    soma += valor
print(f'Você digitou {cont} valores e a soma dos valores digitados foi {soma}')
