print('\033[0:30:41mMonique Oliveira!\033[m')
#\033[m é o começo da coloração, tanto no inicio quanto no final
#Cada número representa uma cor, em cada posição representa onde essa cor vai atuar.

#Estilo: 0 normal, 1 negrito, 4 sublinhado, 7 inverte
#Cor texto: 30 branco, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 roxo, 36 ciano, 36 cinza
#Cor fundo: igual ao texto, porém: 40, 41...

#Realizando testes
print('\033[4:33:44mMonique Oliveira!\033[m')
print('\033[1:35:43mMonique Oliveira!\033[m')
print('\033[30:42mMonique Oliveira!\033[m')
print('\033[mMonique Oliveira!\033[m') #fundo negro
print('\033[7:30mMonique Oliveira!\033[m')

#sem o /033[m a cor segue por todo o código.

a=3
b=5
print('Os valores são \033[32m{} e \033[31m{}.'.format(a, b))

#No exemplo acima a cor amarela no 1º nº e na letra 'e'. No 2º foi no nº e vai no inicio da proxima frase.

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!'.format(a, b))

nome = 'monique'
print('Ei! Muito prazer em te conhecer, {}!'.format('\033[41:34m', nome, '\033[m'))