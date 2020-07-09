from random import choice
from time import sleep
print('Vamos sortear um aluno para começar a aula!')
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi... ')
sleep(3)
print('{}!'.format(escolhido))