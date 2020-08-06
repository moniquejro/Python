print('~*'*20)
print('Analisando triângulos')
print('~*'*20)
r1 = float(input('1º: '))
r2 = float(input('2º: '))
r3 = float(input('3º: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo.')
