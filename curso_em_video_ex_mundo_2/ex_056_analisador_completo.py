"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

idades = media = 0
maior_idade = 0
menor = 0
nome_homem = ''
# laço para pedir as 4 pessoas
for pessoa in range(1, 5):
    print('*' * 20, f'{pessoa}º pessoa', '*' * 20)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F, M]: ')).upper()
    # soma as idades pra depois fazer as médias
    idades += idade
    # inicializa a variavel maior_idade se caso a 1ª pessoa do laço for homem,
    if pessoa == 1 and sexo == 'M':
        maior_idade = idade
        nome_homem = nome
    # senão na proxima iteração, se a pessoa for homem e a idade for maior que a idade anterior ele substitui
    else:
        if idade > maior_idade and sexo == 'M':
            maior_idade = idade
            nome_homem = nome
    # verifica se a idade da mulher é menor de 20 anos, se for ele adiciona mais um na contagem
    if idade < 20 and sexo == 'F':
        menor += 1

media = idades / 4
print(f'A media das idades desse grupo foi de {media}')
print(f'O homem mais velho se chama {nome_homem.upper()} e tem {maior_idade} anos')

if menor == 0:
    print('Não temos mulheres menores de 20 anos')
elif menor == 1:
    print(f'E temos {menor} mulher menor de 20 anos')
else:
    print(f'E temos {menor} mulheres menores de 20 anos')
