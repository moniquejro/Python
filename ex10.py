real= float(input('Quanto de dinheiro você tem na carteira? ->'))
dolar= real/5.21
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(real, dolar))

# :.f é referente a quantas casas decimais você quer depois da vírgula