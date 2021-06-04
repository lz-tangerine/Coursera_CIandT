from math import sin, tan, cos, radians
angulo = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {angulo} tem o seno de {sin(radians(angulo)):.2f}')
print(f'O angulo de {angulo} tem o conseno de {cos(radians(angulo)):.2f}')
print(f'O angulo de {angulo} tem a tangente de {tan(radians(angulo)):.2f}')
