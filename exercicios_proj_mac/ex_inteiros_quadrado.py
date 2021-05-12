# Dada uma seqüência de números inteiros não-nulos, seguida por 0, imprimir seus quadrados.

def main():
  print('Digite uma sequencia de numeros, terminados em zero, para saber seus valores ao quadrado')
  num = int(input('Digite um numero: '))
  while num != 0:
    quadrado = num ** 2
    print('O {} ao quadrado é {}!'.format(num, quadrado))
    num = int(input('Digite um numero: '))

main()
        
