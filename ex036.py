valorC = float(input('Qual o valor da casa?'))
valorS = float(input('Qual é o seu salário?'))
anos = float(input('Quantos anos pra pagar?'))
meses = anos*12
parcela = valorC/meses
porcSal = valorS*0.30
if parcela > porcSal:
    print('Emprestimo negado!')
else:
    print('Emprestimo LIBERADO!')
print('A casa é no valor de {:.2f} reais \nO salário é no valor de {:.2f} reais \nVai ser paga em {} anos \nO valor da parcela vai ser de {:.2f}\n 30% do seu salário é {}'.format(valorC, valorS, anos, parcela, porcSal ))
