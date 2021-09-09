"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""

print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)

total_compra = mais_mil = menor_valor = cont = 0
produto_mais_barato = ''

while True:
    produto = str(input('NOME DO PRODUTO: ')).upper()
    preco = float(input('PREÇO R$ '))
    cont += 1

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('ESCOLHA [S] PARA DIGITAR MAIS PRODUTOS E [N] PARA SAIR ')).strip().upper()[0]
    print('')
    total_compra += preco

    if preco >= 1000:
        mais_mil += 1

    if cont == 1 or preco < menor_valor:
        menor_valor = preco
        produto_mais_barato = produto

    if escolha == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total de compras foi {total_compra:.2f}')
print(f'Temos {mais_mil} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produto_mais_barato} custando {menor_valor:.2f}')
