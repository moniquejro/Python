from time import sleep
num = int(input('Informe um número:  '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}.'.format(num))
sleep(3)
print('Unidade: {}'.format(u))
sleep(1)
print('Dezena: {}'.format(d))
sleep(1)
print('Centena: {}'.format(c))
sleep(1)
print('Milhar: {}'.format(m))