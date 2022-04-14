lista = [2, 4, 2, 2, 3, 3, 1]


def remove_repetidos(lista):
    lista_ordenada = []
    for n in lista:
        if n in lista_ordenada:
            continue
        lista_ordenada.append(n)
    return sorted(lista_ordenada)


remove_repetidos(lista)
