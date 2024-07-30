'''Crie um programa que faça o computador jogar Jokenpô com você.'''

from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

jogador = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Qual é a sua jogada?'''))

if 0 <= jogador <=2:

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    print('-=' * 11)
    print('Computador jogou {}\nJogador jogou {}'.format(itens[computador], itens[jogador]))
    print('-=' * 11)

    if jogador == 0:
        if computador == 0:
            print('EMPATE')
        elif computador == 1:
            print('COMPUTADOR VENCE')
        elif computador == 2:
            print('JOGADOR VENCE')

    elif jogador == 1:
        if computador == 0:
            print('JOGADOR VENCE')
        elif computador == 1:
            print('EMPATE')
        elif computador == 2:
            print('COMPUTADOR VENCE')

    elif jogador == 2:
        if computador == 0:
            print('COMPUTADOR VENCE')
        elif computador == 1:
            print('JOGADOR VENCE')
        elif computador == 2:
            print('EMPATE')

else:
    print('JOGADA INVALIDA')
