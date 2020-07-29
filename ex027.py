#Esse programa vai ler seu nome completo,
#em seguida vai mostrar o primo e o ultimo nome separados.

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer, {}!'.format(nome[0]))
print('Seu primeiro nome é -> {}'.format(nome[0]))
print('Seu último nome é -> {}'.format(nome[len(nome)-1]))
