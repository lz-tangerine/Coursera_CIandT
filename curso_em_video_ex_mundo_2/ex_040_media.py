"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida: Média abaixo de 5.0: REPROVADO, Média entre 5.0 e 6.9: RECUPERAÇÃO;
Média 7.0 ou superior: APROVADO"""

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'A média entre as notas {nota1} e {nota2} é {media}\nO aluno foi REPROVADO!')
elif 5.0 <= media <= 6.9:
    print(f'A média entre as notas {nota1} e {nota2} é {media:.2f}\nO aluno está de RECUPERAÇÃO!')
else:
    print(f'A média entre as notas {nota1} e {nota2} é {media:.2f}\nO aluno foi APROVADO!')