#Aula 12 é sobre condições aninhadas. Exatamente como o exemplo abaixo: várias condições dentro da outra.
#Fiz uma brincadeira com o nome da minha namorada e pessoas conhecidas, não levem a mal.

nome = str(input('Qual seu nome?  --->>>   '))
if nome == 'Monique' or nome == 'monique' or nome == 'Monique Oliveira' or nome == 'Monique oliveira' or nome == 'monique oliveira':
    print('Que nome lindo, maravilhoso, {}! \n PER-FEI-CION!'.format(nome))
elif nome in 'Maria Matheus':
    print('Que nome lindo!')
elif nome == 'Fulano' or nome == 'fulano' or nome == 'fulaninho' or nome == 'fulanO':
    print('Isso nem é nome, {}...'.format(nome))
elif nome == 'Viviane':
    print('Esse nome é diferente...')
elif nome == 'Viviane Cordeiro' or nome == 'viviane cordeiro' or nome == 'Cordeiro' or nome == 'Viviane cordeiro':
    print('Solidão né minha filha...')
elif nome == 'vivi':
    print('Solidão né minha filha...')
print('Tenha um bom dia, {}!'.format(nome))
