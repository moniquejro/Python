import time
print('~~'*15)
print(' '*10,'TABUADA')
n = float(input("Um nº entre 0 e 10: "))
for c in range (0, 11):
    r = n*c
    letra = str()
    print('{} x {:.2f} = {:.1f}'.format(c, n, r))
    time.sleep(1)
print('~~'*15)