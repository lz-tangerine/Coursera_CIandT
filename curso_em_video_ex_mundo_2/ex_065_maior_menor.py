"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve
perguntar ao usuário se ele quer ou não continuar a digitar valores."""

soma = media = contador = 0
menor = maior = 0
resposta = str('Ss')
while resposta in 'Ss':
    valor = int(input('Digite um número: '))
    soma += valor
    contador += 1
    if contador == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
    resposta = str(input('Quer continuar? [S/N]: '))
media = soma / contador
print(f'Você digitou {contador} numeros e a média foi {media}')
print(f'O maior valor digitado foi {maior} e o menor valor foi {menor}')
