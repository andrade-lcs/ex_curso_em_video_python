from random import randint
n = randint(1,10)
print('A tabuada no número {}:'.format(n))
for m in range(1,11):
    print('{}x{}={}'.format(n,m,n*m))
print('FIM')