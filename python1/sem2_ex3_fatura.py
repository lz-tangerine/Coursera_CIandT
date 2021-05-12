#Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente,
# o dia de vencimento, o mês de vencimento e o valor da fatura  e imprima
# (saída de dados) a mensagem com os dados recebidos, no mesmo formato da mensagem acima.

cliente = input('Digite o nome do cliente: ')
dia_vencimento = int(input('Digite o dia de vencimento: '))
mes_vencimento = input('Digite o mês de vencimento: ')
valor_fatura = input('Digite o valor da fatura: ')

print('Olá, {}'.format(cliente))

print('A sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.'.format(dia_vencimento, mes_vencimento, valor_fatura))
