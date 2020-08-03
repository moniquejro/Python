#Crie um programa que leia qualquer ano e indique se ele é BISSEXTO!

from datetime import date
ano = int(input('Digite o ano que você deseja analisar e \ndigite 0 para analisar o ano atual. -> '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    #O ano bissexto tem algumas regras que são:
    #ocorre de 4 em 4 anos, EXCETO multiplos de 100 que NÃO SÃO multiplos de 400.
    
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} NÃO é bissexto!'.format(ano))
