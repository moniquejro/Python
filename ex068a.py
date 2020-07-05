from random import randint
v = 0
while True:
    player = int(input("Vamos brincar de par ou ímpar? Escolha um número! -> "))
    pc = randint(0, 10)
    total = player + pc
    tipo = ' '
    while tipo not in "PI":
            tipo = str(input('Você quer par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {player} e o computador {pc}. A soma dá {total}! ', end='')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
             print('Você perdeu!')
             break
    elif tipo == 'I':
        if total % 2 == 1:
             print('Você venceu!')
             v += 1
        else:
             print('Você perdeu!')
             break
    print('Vamos de novo...?')
print(f'Game over! Você venceu {v} vezes.')