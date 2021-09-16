"""Usando f antes da string para usar as variaveis ao inves de .format
o ^20 depois do nome é para centralizar o nome dentro de 20 espaços e .2f dentro de salario é para colocar
2 numeros após a virgula"""

nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome:^20} tem {idade} anos e ganha R$ {salario:.2f}')
print('{:-^40}'.format('Fim do programa'))

soma = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor == 999:
        break
    soma += valor

n = 'uber'
if n[0] in 'aeiou':
    print(n)
