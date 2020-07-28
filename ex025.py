#Crie um programa que leia o nome de uma pessoa e
#diga se ela tem "OLIVEIRA" no nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Oliveira? {}'.format('oliveira' in nome.lower()))
