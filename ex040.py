#AQui vamos analisar uma nota e ver se o aluna(o) foi aprovada(o)

import time #importar calendario, data e etc
print('<>'*25)
n1 = float(input('\033[1mPrimeira nota --->>>\033[m'))
n2 = float(input('\033[1mSegunda nota --->>>\033[m'))
m = (n1+n2)/2
print('PROCESSANDO...')
time.sleep(3) #suspense
if m < 5.0:
    print('\033[1:41mREPROVADO com média {}!\033[m'.format(m))
elif m >=5.0 and m <=6.9:
    print('\033[Ninguém liga com essa média de {}\033[m'.format(m))
else:
    print('\033[1:46mAPROVADO\033[m\n\033[1:44mMÉDIA {}\033[m'.format(m))
print('\033[7m1ª Nota: {}\033[m'.format(n1))
print('\033[7m2ª Nota: {}\033[m'.format(n2))
print('<>'*25)
