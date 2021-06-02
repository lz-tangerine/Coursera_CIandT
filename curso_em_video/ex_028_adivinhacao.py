from time import sleep
from random import randint
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
numero_escolhido = randint(1, 5)
tentativa = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if tentativa == numero_escolhido:
    print('VOCÊ ACERTOU!!!')
else:
    print(f'VOCÊ ERROU!!! Eu pensei no número {numero_escolhido}')



