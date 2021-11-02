for c in range (0,51, 2):
    print(c, end= '-') #sequencia na mesma linha
print('acabou')
#a forma acima é um programa mais curto e que faz a mesma coisa que o de baixo
#outra forma

for c in range(1, 51):
    if c % 2 == 0:
            print(c, end=' ')
print('Acabou')
