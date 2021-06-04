salario = float(input('Qual salário do funcionario? \nR$ '))
aumento = salario + ((salario * 15) / 100)
print(f'Um funcionario que ganhava R$ {salario}, com 15% de aumento, passa a receber R$ {aumento:.2f}.')
