#O mesmo professor do exercício 19 quer sortear
#a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.

from random import shuffle
n1 = str(input('Nome do 1º aluno: '))
n2 = str(input('Nome do 2º aluno: '))
n3 = str(input('Nome do 3º aluno: '))
n4 = str(input('Nome do 4º aluno: '))

lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
