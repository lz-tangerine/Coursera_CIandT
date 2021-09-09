inicio = int(input("Inicio: "))
fim = int(input("Fim: "))

if inicio < fim:
    while inicio <= fim:
        print('{}... '.format(inicio), end='')
        inicio += 1
else:
    while inicio >= fim:
        print('{}... '.format(inicio), end='')
        inicio -= 1

