#Faça um programa que leia 3 números e mostre
#qual deles é o maior e qual é o menor.

print('~*'*32)
print('\nDigite 3 números e vamos ver qual é o maior e qual é o menor!')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

#Verificando qual é o maior

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#Verificando quem é o maior

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor digitado foi {}!'.format(menor))
print('O maior valor digitado foi {}!\n'.format(maior))

print('~*'*32)
