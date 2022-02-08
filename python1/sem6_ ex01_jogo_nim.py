def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        quantia = n % (m + 1)
        if quantia > 0:
            return quantia
        return m


def usuario_escolhe_jogada(n, m):
    while True:
        jogada = int(input('Quantas peças você vai tirar? '))
        if jogada > n or jogada < 1 or jogada > m:
            print('Oops! Jogada inválida! Tente de novo.')
        else:
            return jogada

def partida():
    n = int(input('Quantas peças: '))
    m = int(input('Limite de peças por jogada: '))
    partida_ganha_usuario = 0
    partida_ganha_computador = 0

    if n % (m + 1) == 0:
        print('\nVocê começa!')

        while True:
            escolha_usuario = usuario_escolhe_jogada(n, m)
            n -= escolha_usuario
            print(f'\nVocê tirou {escolha_usuario} peça(s)')
            if n == 0:
                print('Fim do jogo! Você ganhou!\n')
                partida_ganha_usuario += 1
                break
            print(f'Agoram restam {n} peça(s) no tabuleiro\n')

            escolha_computador = computador_escolhe_jogada(n, m)
            n -= escolha_computador
            print(f'\nComputador tirou {escolha_computador} peça(s)')
            if n == 0:
                print('Fim do jogo! O computador ganhou!\n')
                partida_ganha_computador += 1
                break
            print(f'Agoram restam {n} peça(s) no tabuleiro\n')

        placar_usuario = partida_ganha_usuario
        placar_computador = partida_ganha_computador

    else:
        print('\nComputador começa!!')

        while True:
            escolha_computador = computador_escolhe_jogada(n, m)
            n -= escolha_computador
            print(f'Computador tirou {escolha_computador} peça(s)')
            if n == 0:
                print('Fim do jogo! O computador ganhou!\n')
                partida_ganha_computador += 1
                break
            print(f'Agora restam {n} peça(s) no tabuleiro\n')

            escolha_usuario = usuario_escolhe_jogada(n, m)
            n -= escolha_usuario
            print(f'Você tirou {escolha_usuario} peça(s)')
            if n == 0:
                print('Fim do jogo! Você ganhou!\n')
                partida_ganha_usuario += 1
                break
            print(f'Agora restam {n} peça(s) no tabuleiro\n')

        placar_usuario = partida_ganha_usuario
        placar_computador = partida_ganha_computador

    return placar_usuario, placar_computador


def campeonato():
    placar_usuario = 0
    placar_computador = 0
    print('\nVocê escolheu uma campeonato!\n')

    for i in range(1, 4):
        print(f'***** Rodada {i} *****')
        p_u, p_c = partida()
        placar_usuario += p_u
        placar_computador += p_c

    print(f'{" Final de Campeonato ":*^60}')
    print(f'Placar: Você {placar_usuario} X {placar_computador} Computador')


def main():
    while True:
        choice = int(input(('Bem vindo ao jogo do NIM! Escolha: \n\n'
                            '[ 1 ] Para jogar uma partida isolada\n'
                            '[ 2 ] Para jogar um campeonato\n'
                            'Sua escolha: ')))
        if choice == 1:
            print('\nVocê escolheu uma partida!\n')
            partida()
            break

        elif choice == 2:
            campeonato()
            break

        else:
            print('Escolha invalida! Tente novamente!\n')


main()
