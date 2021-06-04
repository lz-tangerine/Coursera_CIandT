"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

valor_casa = float(input('Digite o valor do empréstimo: R$ '))
salario = float(input('Digite o valor do seu sálario bruto: R$ '))
parcela = int(input('Digite em quantos anos gostaria de pagar: R$ '))
calculo_mes = parcela * 12
calculo_porcentagem = salario - (salario * 30 / 100)
prestacao_mensal = valor_casa / calculo_mes
aprovado = prestacao_mensal if prestacao_mensal <= calculo_porcentagem else False
if aprovado:
    print(f'Seu emprestimo foi APROVADO! Você pagará {calculo_mes} parcelas de R${prestacao_mensal:.2f} por mês.')
else:
    print(f'Sinto muito mas seu empréstimo foi NEGADO! Sua parcela de R${prestacao_mensal:.2f} excede 30% do '
          f'valor do seu salario!')