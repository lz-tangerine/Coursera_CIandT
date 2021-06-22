"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento: – à vista dinheiro/cheque: 10% de desconto, – à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal, – 3x ou mais no cartão: 20% de juros"""
valor = float(input('Valor das compras: R$ '))
print('='*30)
print('FORMAS DE PAGAMENTO\n'
      '[ 1 ] à vista dinheiro\n'
      '[ 2 ] à vista cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no cartão')
print('')
opcao = int(input('Digite a opção desejada: '))
if opcao == 1:
    print(f'Sua compra de R${valor:.2f} vai custar R${valor - (valor * 10 / 100):.2f} com desconto de 10%! ')
elif opcao == 2:
    print(f'Sua compra de R${valor:.2f} vai custar R${valor - (valor * 5 / 100):.2f} com desconto de 5%! ')
elif opcao == 3:
    print(f'Sua compra de R${valor:.2f} não tem desconto nessa oção de pagamento!')
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcela}x de R$ {(valor + (valor * 20 / 100)) / parcela:.2F} COM JUROS\n'
          f'O preço final será de R${valor + (valor * 20 / 100):.2f}!')
else:
    print('Opção inválida! Tente novamente!')
