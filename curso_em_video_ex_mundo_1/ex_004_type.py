frase = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(frase)}')
print(f'Só tem espaços? {frase.isspace()}')
print(f'É um número? {frase.isnumeric()}')
print(f'É alfabético? {frase.isalnum()}')
print(f'É alfanumerico? {frase.isalpha()}')
print(f'Está em maiusculas? {frase.isupper()}')
print(f'Está em minuscula? {frase.islower()}')
print(f'Está capitalizada? {frase.istitle()}')
