"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

soma = 0
valores = 0
total_valores = 0
while valores != 999:
    valores = int(input("Digite um número [999 para parar]: "))
    if valores != 999:
        soma += valores
        total_valores += 1
print('Voce digitou {} valores e a soma dos valores digitados foi de {}'. format((total_valores), (soma)))
