#Crie um programa que leia uma frase e mostre:
#1: quantas vezes aparece a letra A;
#2: em que posição ela aparece a primeira vez;
#3: em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra A aparece a primeira vez na posição {}.'.format(frase.find('A')+1))
print('A letra A aparece a última vez na posição {}.'.format(frase.rfind('A')+1))
