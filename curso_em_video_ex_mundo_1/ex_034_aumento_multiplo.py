salario = float(input('Qual sálario do funcionario: R$ '))
aumento = (salario * 15 / 100) + salario if salario <= 1250 else (salario * 10 / 100) + salario
print(f'Quem recebia R${salario:.2f}, passa a receber R${aumento:.2f}')

