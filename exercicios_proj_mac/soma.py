#Dada uma sequência de números inteiros diferentes de zero,
# terminada por um zero, calcular a sua soma.

def main():
    entrada = int(input('Digite um numero para a soma: '))
    soma = 0
    while entrada != 0:
        soma += entrada
        entrada = int(input('Digite um numero para a soma: '));        
    print('A soma dos numeros foi de', soma)

main()
