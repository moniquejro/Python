from datetime import date
atual = date.today().year
nasc = int(input('Informe o ano de nascimento: '))
idade = atual - nasc
print('A pessoa que nasceu no ano de {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar no exército e também pode tirar CNH!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para você tirar CNH e se alistar no exército!'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento e a CNH será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado e retirado a CNH a {} anos!'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))