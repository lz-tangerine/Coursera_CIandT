import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas [-1] == '':
        del sentencas [-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase.'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez.
    Razão Hapax Legomana'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq [p] == 1:
                unicas -= 1
            freq [p] += 1
        else:
            freq [p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas.'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq [p] += 1
        else:
            freq [p] = 1
    return len(freq)


def tamanho_medio_palavra(frase):
    '''é a soma do tamanho das palavras dividida pelo número total de palavras.'''
    i = 0
    for caracter in separa_palavras(frase):
        for letra in caracter:
            if letra in '.,?!:;':
                i -= 1
        i += len(caracter)
    palavras = len(separa_palavras(frase))
    return i / palavras


def type_token(frase):
    '''é o número de palavras diferentes dividido pelo número total de palavras.'''
    palavras_diferentes = n_palavras_diferentes(separa_palavras(frase))
    quantidade_palavras = len(separa_palavras(frase))
    return palavras_diferentes / quantidade_palavras


def hapax_legomana(frase):
    quantidade_palavras_unicas = n_palavras_unicas(separa_palavras(frase))
    quantidade_palavras = len(separa_palavras(frase))
    return quantidade_palavras_unicas / quantidade_palavras


def tamanho_medio_sentencas(texto):
    """é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças"""
    i = 0
    for caracter in separa_palavras(texto):
        for letra in caracter:
            if letra in '.,?!:;':
                i -= 1
        i += len(caracter)
    return i / len(separa_sentencas(texto))


lista_frases = []


def complexidade_sentencas(texto):
    """é o número total de frases divido pelo número de sentenças"""
    sentencas = separa_sentencas(texto)
    for s in sentencas:
        frases_separadas = separa_frases(s)
        for frases in frases_separadas:
            lista_frases.append(frases)
    return len(lista_frases) / len(sentencas)


def tamanho_medio_frase(sentenca):
    '''é a soma do número de caracteres em cada frase dividida pelo número de frases no texto'''
    i = 0
    for caracter in separa_palavras(sentenca):
        for letra in caracter:
            if letra in ',:;.!?':
                i -= 1
        i += len(caracter)
    return i / len(lista_frases)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas
    assinaturas. '''
    somatoria = 0
    for traco_linguistico in range(len(as_a)):
        somatoria += abs(as_a[traco_linguistico] - as_b[traco_linguistico])
    return somatoria / 6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    return [tamanho_medio_palavra(texto), type_token(texto), hapax_legomana(texto),
            tamanho_medio_sentencas(texto), complexidade_sentencas(texto), tamanho_medio_frase(texto)]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do
    texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    valor = ass_cp[0]
    indice = 0
    for i in range(len(ass_cp)):
        if ass_cp[i] < valor:
            valor = ass_cp[i]
            indice = i
    return indice
