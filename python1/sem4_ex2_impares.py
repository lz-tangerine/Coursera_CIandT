n = int(input('Digite o valor de n: '))
impar = 1
while n > 0:
    if impar % 2 != 0:
        print(impar)
        n -= 1
    impar += 1
