from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        if jogador > 10:
            print('Você digitou {} e é acima de 10. Tente novamente! '.format(jogador))
        if jogador < 0:
            print('Você digitou {} e é um numero negativo. Tente novamente!'.format(jogador))
        elif jogador > computador:
            print('Menos... Tente mais um vez!')
print('Parabéns! Você acertou! Demorou {} tentativas!'.format(palpite))