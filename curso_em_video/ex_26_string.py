frase = str(input('Digite uma frase: ')).strip().upper()
vezes = frase.count('A')
posicao = frase.find('A')+1
ultima_posicao = frase.rfind('A')+1
print(f'A letra A aparece {vezes}x na frase')
print(f'A primeira letra A apareceu na posição {posicao}')
print(f'A ultima letra A apareceu na posição {ultima_posicao}')
