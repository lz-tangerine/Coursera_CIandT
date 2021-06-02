cidade = str(input('Em que cidade você nasceu: ')).rstrip().lstrip().lower()
palavra = 'santo' in cidade
print(f'Essa cidade tem a palavra Santo? {palavra}.')
