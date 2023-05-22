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
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    somatoria = 0
    for traco_linguistico in range(len(as_a)):
        somatoria += abs(as_a[traco_linguistico] - as_b[traco_linguistico])
    return somatoria / 6

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_setencas = []
    lista_frases = []
    lista_palavras = []
    n_caracteres_frase = 0
    n_caracteres = 0
    n_letras = 0
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        lista_setencas.append(sentenca)
        frases = separa_frases(sentenca)
        n_caracteres += len(sentenca)
        for frase in frases:
            lista_frases.append(frase)
            n_caracteres_frase += len(frase)            
            palavras = separa_palavras(frase)
            for palavra in palavras:
                lista_palavras.append(palavra)
            for letras in palavras:
                n_letras += len(letras)
    
    wal_texto = n_letras / len(lista_palavras)
    ttr_texto = n_palavras_diferentes(lista_palavras) / len(lista_palavras)
    hlr_texto = n_palavras_unicas(lista_palavras) / len(lista_palavras)
    sal_texto = n_caracteres / len(lista_setencas)
    sac_texto = len(lista_frases) / len(lista_setencas)
    pal_texto = n_caracteres_frase / len(lista_frases)
    
    return [wal_texto, ttr_texto, hlr_texto, sal_texto, sac_texto, pal_texto]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    ass_cp = ass_cp
    textos = textos
    assinaturas = []
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))
    assinaturas_comparadas = []
    for assinatura in assinaturas:
        assinaturas_comparadas.append(compara_assinatura(ass_cp, assinatura))
    valor = ass_cp[0]
    for textos in range(len(ass_cp)):
        if ass_cp[textos] < valor:
            valor = ass_cp[textos]
            indice = textos        
            return indice+1
    
def main():  
    assinatura = le_assinatura()
    textos = le_textos()
    infectado = avalia_textos(textos, assinatura)
    print(f'O autor do texto {infectado} esta infectado com COH-PIAH')

main()