#Crie um programa que leia um número real
#e mostre qual é sua parte inteira.
#Exemplo:
# Real: 9.4587   Inteiro: 9

from math import trunc
#Aqui como só vai utilizar uma função,
# não tem porquê importar a biblioteca math inteira
# e sim só a utilizada.

num = float(input('Digite um valor real: '))
print('O valor digitado foi {} e a sua parte inteira é {}.'.format(num, trunc(num)))