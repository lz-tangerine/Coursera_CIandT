km_viagem = float(input('Qual é a distancia da sua viagem em km? '))
if km_viagem < 200:
    passagem = km_viagem * 0.50
    print(f'Você está prestes a começar uma viagem de {km_viagem:.1f} km \nE o preço da sua passagem '
          f'será de R${passagem:.2f}')
else:
    passagem = km_viagem * 0.45
    print(f'Você está prestes a começar uma viagem de {km_viagem:.1f} km \nE o preço da sua passagem '
          f'será de R${passagem:.2f}')
