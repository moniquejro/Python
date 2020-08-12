print('\033[1:31m+\033[m\033[1m~\033[m'*20)
print(' '*30,' \033[1m TABELA IMC\033[m')
#print('TABELA IMC'.__len__()) #mostra qnts caracteres tem a str
print('\033[1:37m- Abaixo de 18.5: Abaixo do peso\033[m')
print('\033[1:37m- Entre 18.5 e 25: Peso ideal\033[m')
print('\033[1:37m- Entre 25 e 30: Sobrepeso\033[m')
print('\033[1:37m- Entre 30 até 40: Obesidade\033[m')
print('\033[1:37m- Acima de 40: Obesidade Morbida\033[m')
print('\033[1m~\033[m\033[1:31m+\033[m'*20)
peso = float(input('\033[1:32mInforme seu peso\033[m \033[1:35m~~~>>   \033[m'))
alt = float(input('\033[1:32mInforme sua altura\033[m \033[1:35m~~~>>   \033[m'))
imc = peso/(alt**2)
##
if imc <= 18.5:
    print('\033[1mAbaixo do peso com IMC de\033[m \033[1:34m{:.2f}\033[m\033[1m.\033[m'.format(imc))
elif imc >18.5 and imc <25:
    print('\033[1mPeso ideal com IMC de\033[m \033[1:37m{:.2f}\033[m\033[1m.\033[m'.format(imc))
elif imc >=25 and imc <30:
    print('\033[1mSobrepeso com o IMC de\033[m\033[1:33m {:.2f}\033[m\033[1m.\033[m'.format(imc))
elif imc >=30 and imc <40:
    print('\033[1mObesidade com IMC de\033[m \033[1:31m{:.2f}\033[m\033[:1m.\033[m'.format(imc))
elif imc >= 40:
    print('\033[1mObesidade mórbida.\033[m\033[1:31m Procure um profissional da saúde!\033[m\033[1m,\npq seu IMC é de\033[1:47m {:.2f}\033[m\033[1m!\033[m'.format(imc))
print('\033[1:31m+\033[m\033[1m~\033[m'*20)