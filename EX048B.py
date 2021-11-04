soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 ==0:
        cont = cont + 1 # tb pode ser  -> cont+= 1
        soma = soma + c# tb pode ser -> soma += c
print('A soma de {} valores é igual a {}!'.format(cont, soma))
