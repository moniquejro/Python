#Desenvolva um programa que analise a distância de uma viagem em quilometros
#Calcule o preço da passagem, cobrando R$0,50 por quilometro para viagens de até
#200km e R$0,45 para viagens mais longas.

km = float(input('Qual é a distância da sua viagem? '))
print('Você vai realizar uma viagem de {} km!'.format(km))
preco = km * 0.50 if km <= 200 else km * 0.45
print('O valor da sua passagem é de R${:.2f}!'.format(preco))
