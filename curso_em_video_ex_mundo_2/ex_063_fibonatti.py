num_anterior = 0
fibonatti = 1

termo = int(input('Digite a quantidade de termos a serem mostrador: '))
contador = 0
while contador < termo:
    num_anterior += fibonatti
    fibonatti = num_anterior - fibonatti
    print(fibonatti, end=' ')
    contador += 1
