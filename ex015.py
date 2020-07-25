#Esse programa vai receber a quantidade de dias
#e a quilometragem rodada com o carro alugado.
#Vai ser calculado o preço a ser pago, sabendo que
#R$60 o dia e R$0,015 por quilometro rodado.

dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos KM rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a ser pago é de R${:.2f}.'.format(pago))