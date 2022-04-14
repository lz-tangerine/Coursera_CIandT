numero_usuario = []
while True:
    digitado = (int(input('Digite uma sequencia de numeros terminadas por 0: ')))
    numero_usuario.append(digitado)
    if digitado == 0:
        numero_usuario.pop()
        break
ordem_inversa = len(numero_usuario) - 1
while ordem_inversa >= 0:
    print(numero_usuario[ordem_inversa])
    ordem_inversa -= 1
