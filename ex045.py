from time import sleep
from random import randint
choice = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print(''''Escolha:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
player = int(input('\nQual você escolhe? '))
print('~~'*15)
print('O computador escolheu {}!'.format(choice[pc]))
print('Você escolheu {}!'.format(choice[player]))
print('~~'*15)
if pc == 0: #pc jogou pedra
    if player == 0:
        print('Empate!')
    elif player == 1:
        print('Você ganhou!')
    elif player == 2:
        print('Você perdeu!')
    else:
        print('Jogada inválida!')
elif pc == 1: #pc jogou papel
    if player == 0:
        print('Você perdeu!')
    elif player == 1:
        print('Empate!')
    elif player == 2:
        print('Você ganhou!')
    else:
        print('Jogada inválida!')
elif pc == 2: #pc jogou tesoura
    if player == 0:
        print('Você ganhou!')
    elif player == 1:
        print('Você perdeu!')
    elif player == 2:
        print('Empate!')
    else:
        print('Jogada inválida!')
