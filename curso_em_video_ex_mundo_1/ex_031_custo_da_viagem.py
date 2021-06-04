km_viagem = float(input('Qual é a distancia da sua viagem em km? '))
print(f'Você está prestes a começar uma viagem de {km_viagem:.1f} km')
passagem = km_viagem * 0.50 if km_viagem <= 200 else km_viagem * 0.45
print(f'E o preço da sua passagem será de R${passagem:.2f}')
