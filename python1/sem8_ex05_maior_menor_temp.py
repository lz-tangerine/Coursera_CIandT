'''def importar_csv(file):
    import csv
    with open(file, 'r', encoding='ISO-8859-1') as arquivo_csv:
        arquivo_csv = csv.reader(file, delimiter=';')

    return arquivo_csv

import csv
with open('caracteristicas-muncipais_novo.csv', 'r', encoding='ISO-8859-1') as file:
    file_csv = csv.reader(file, delimiter=';')
    for i, line in enumerate(file_csv):
        if i == 1:
            higher_temp = line[8]
            lower_temp = line[9]
            higher_county = line[1]
            lower_county = line[1]
        else:
            if i != 0:
                if line[8] > higher_temp:
                    higher_temp = line[8]
                    higher_county = line[1]
                elif line[9] < lower_temp and line[9] != '':
                    lower_temp = line[9]
                    lower_county = line[1]

    print(f'O municipio de {lower_county} tem a menor temperatura com {lower_temp}')
    print(f'O municipio de {higher_county} tem a maior temperatura com {higher_temp}')'''

import csv
with open('Inventario_Hive.csv', 'r') as hive:
    hive_csv = csv.reader(hive, delimiter=',')
    for i, line in enumerate(hive):
        if i == 1:
            database = line[1]

print(database)

