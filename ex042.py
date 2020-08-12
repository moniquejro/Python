from time import sleep
print('\033[1:32mInforme 3 valores para serem analisados!\033[m')
r1 = float(input('1º valor: '))
r2 = float(input('2º valor: '))
r3 = float(input('3º valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Vou pensar... \nOs segmentos acima podem formar um triângulo do tipo... ', end='')
    sleep(2)
    if r1 == r2 == r3:
        print('\n\033[1:31mEquilátero!\033[m')
    elif r1 != r2 != r3 != r1:
        print('\n\033[1:31mEscaleno!\033[m')
    else:
        print('\n\033[1:31mIsósceles!\033[m')
else:
    print('Os segmentos acima \033[1:31mnão\033[m podem formar um triângulo.')