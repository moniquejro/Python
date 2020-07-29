from random import randint
from time import sleep
computador = randint(0, 5) #faz o pc 'pensar'
print('~*'*18)
print('Vou pensar em um número entre 0 e 5. \nTente adivinhar...')
print('~*'*18)
jogador = int(input('Em que número pensei? ')) #jogador tenta adivinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu adivinhar!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))