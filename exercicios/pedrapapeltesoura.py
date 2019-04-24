"""
pedrapapeltesoura.py

Faça um jogo de Pedra, Papel e Tesoura para dois jogadores. O programa 
deve pedir que cada jogador digite sua jogada. Em seguida, deve 
comparar as jogadas, mostrar uma mensagem de parabéns ao vencedor e 
perguntar se os jogadores querem começar uma nova partida.
"""

jogar = 's'

while jogar == 's':
    print()
    print('Jogadas válidas: "pedra", "papel" ou "tesoura"')
    print()
    j1 = input('Jogador 1: ')
    j2 = input('Jogador 2: ')
    print()

    if j1 == 'pedra' and j2 == 'papel':
        print('Jogador 2 venceu. Parabéns!')
    elif j1 == 'pedra' and j2 == 'tesoura':
        print('Jogador 1 venceu. Parabéns!')
    elif j1 == 'papel' and j2 == 'pedra':
        print('Jogador 1 venceu. Parabéns!')
    elif j1 == 'papel' and j2 == 'tesoura':
        print('Jogador 2 venceu. Parabéns!')
    elif j1 == 'tesoura' and j2 == 'papel':
        print('Jogador 1 venceu. Parabéns!')
    elif j1 == 'tesoura' and j2 == 'pedra':
        print('Jogador 2 venceu. Parabéns!')
    else:
        print('Jogada inválida!')

    print()
    jogar = input('Jogar novamente? (s/n) ')

print('Fim de jogo.')


    
    
