from math import trunc

n = int(input('Digite um número inteiro: '))
b=0
for c in range(1,n+1):
    if n % c ==0:
        print('\033[33m', end='')
        b=b+1
    else:
        print('\033[31m', end='')
    print('{} '.format(c),end='')
if b ==2:
    print('\n\033[mO número {} é primo'.format(n))

print('FIM')