"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""

print('*'*30)
print('{:^30}'.format('CADASTRO DE PESSOAS'))
print('*'*30)
total_pessoas = maior_idade = homens = mulheres = 0

while True:
    idade = int(input('IDADE: '))
    genero = ' '
    while genero not in 'FfMm':
        genero = str(input('GENERO [M/F]: ')).strip().upper()[0]
    print(' ')

    if idade >= 18:
        total_pessoas += 1
    if genero == 'M':
        homens += 1
    if genero == 'F' and idade >= 20:
        mulheres += 1

    escolha = ' '
    while escolha not in 'SsNn':
        escolha = str(input('ESCOLHA [S] PARA CADASTRAR MAIS UMA PESSOA E [N] PARA SAIR: ')).strip().upper()[0]

    if escolha == 'N':
        break
    print('*' * 30)

print(f'O total de pessoas cadastradas com mais de 18 anos foi(ram) {total_pessoas} ')
print(f'Ao todo temos {homens} homem(ns) cadastrado(s)')
print(f'E temos {mulheres} mulher(es) com menos de 20 anos')
