cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adj = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adj ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')
