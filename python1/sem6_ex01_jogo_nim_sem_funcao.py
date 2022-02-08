choice = int(input('Bem vindo ao jogo do NIM! Escolha:\n'
                   '[ 1 ] Para partida isolada\n'
                   '[ 2 ] Para campeonato\n'
                   'Sua escolha: '))

if choice == 1:
    print('\nVocê escolheu partida!\n\n')
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))

    if n % m == 0 + 1:
        print('\nVocê começa!')
        usuario_jogada = int(input('Quantas peças você vai tirar? '))
        n -= usuario_jogada

    else:
        print('\nComputador começa!\n')
        if n % m == 0 + 1:
            computador_jogada = n - 1
        else:
            computador_jogada = n - 2

    while n != 0:
        usuario_jogada = int(input('Quantas peças você vai tirar? '))
        n -= usuario_jogada



