from datetime import  date
anoAtt = date.today().year
print('\033[1m~\033[m'*45)
print('\033[4:32mCATEGORIA POR IDADE\033[m')
print('\033[1mAté\033[m \033[1:33m9 anos\033[m: \033[1:34mMIRIM\033[m \n\033[1mAté\033[m \033[1:33m14 anos\033[m: \033[1:34mINFANTIL\033[m ')
print('\033[1mAté\033[m \033[1:33m19 anos\033[m: \033[1:34mJUNIOR\033[m \n\033[1mAté\033[m \033[1:33m20 anos\033[m: \033[1:34mSENIOR\033[m \n\033[1mAcima\033[m: \033[1:34mMASTER\033[m')
print('\033[1m~\033[m'*45)
anoNas = int(input('\033[1mDigite o ano em que você nasceu\033[m \033[1:33m===>\033[m'))
cat = anoAtt-anoNas
if cat <= 9:
    print('Você tem {} anos'.format(cat))
    print('Sua categoria é: \033[1:34mMIRIM\033[m')
elif cat >9 and cat <=14:
    print('Você tem {} anos'.format(cat))
    print('Sua categoria é: \033[1:34mINFANTIL\033[m')
elif cat >14 and cat <=19:
    print('Você tem {} anos'.format(cat))
    print('Sua categoria é: \033[1:34mJUNIOR\033[m')
elif cat >19 and cat <=20:
    print('Você tem {} anos'.format(cat))
    print('Sua categoria é: \033[1:34mSENIOR\033[m')
else:
    print('Você tem {} anos'.format(cat))
    print('Sua categoria é: \033[1:34mMASTER\033[m')
print('\033[1:31mEstamos no ano de {}\033[m'.format(anoAtt))
print('\033[1m~\033[m'*45)