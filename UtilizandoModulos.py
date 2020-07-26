import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}.'.format(num, raiz))

#print('Arredondando para cima: ')
#print('A raiz de {} é igual a {}.'.format(num, math.ceil(raiz)))

#print('Arredondando para baixo: ')
#print('A raiz de {} é igual a {}.'.format(num, math.floor(raiz)))

#print('Outra forma de formatação: ')
#print('A raiz de {} é igual a {:.2f}.'.format(num, raiz))

#Outra maneira é fazer from math import (aparecerá várias opções específicas)

#from math import sqrt
#desse modo traz a função direta, não precisa fazer citação, como foi feito acima

#from mth import sqrt
#num = int(input('Digite um número: '))
#raiz = sqrt(num) /a mudança ocorreu aqui/
#print('A raiz de {} é igual a {}.'.format(num, raiz))

#Caso eu queira mais de uma função da biblioteca
#eu chamo separando por vírgulas

#from math import sqrt, floor   /a mudança ocorreu aqui/
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a {}.'.format(num, floor(raiz)))

#indo ao site do python.org vc encontra as atualizações e
#na parte de DOCS está disponível, entre muitas coisas, a seção de 'library reference'
#na seção math existem todas as funcionalidades disponíveis e como usar.

#A função random é de escolha ao acaso de um número:
#import random
#num = ramdom.random()
#print(num)

#Assim é escolhido um número inteiro
#import random
#num = ramdom.randint(1, 10)  /entre 1 e 10/
#print(num)

#Se você tiver curiosidade, pode digitar "import" + ctrl espaço
#vai aparecer todas as bibliotecas disponíveis para importar

#Voltando ao site python.org e clicando na parte de PyPI,
#você vai encontrar um index de pacotes extras!
#você pode criar sua própria biblioteca e disponibilizar,
#além de importar as que foram criadas por outros usuários
