print('{:=^40}'.format(' MERCADO DA MONIQUE '))
preco = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA CARTAO
[ 3 ] 2x NO CARTAO
[ 4 ] 3x OU MAIS NO CARTAO''')
opcao = int(input('Qual é a opcao?'))
if opcao ==1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS!'.format(totparc,parcela))
else:
    total = preco
    print('OPCAO INVALIDA DE PAGAMENTO. TENTE NOVAMENTE!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
