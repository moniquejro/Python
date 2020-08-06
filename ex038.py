n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior!')
elif n2 > n1:
    print('O SEGUNDO valor é maior!')
#Como não existe uma quarta opção, não é necessário elif n1 == n2
else:
    print('Os valores são iguais!')