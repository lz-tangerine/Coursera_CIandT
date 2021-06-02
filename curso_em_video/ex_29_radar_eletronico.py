velocidade = float(input('Qual é a velocidade atual do carro: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h \nVocê deve pagar uma multa de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')

