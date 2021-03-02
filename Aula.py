'''for c in range (1, 10):
    print(c)
print('FIM')
c = 1
while c < 11 :
    print(c)
    c = c + 1
print('FIM')
for c in range (1 , 5):
    n=int(input('Digite um valor: '))
print('FIM')
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r =str(input('Quer continuar digite S ou N: ').upper())
print('FIM')
n = 1
p = 0
i = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            p += 1
        else:
            i += 1
print('Você digitou {} pares e {} impares.'.format(p, i))
print('FIM')
from time import sleep
c = 1
while True:
    print(c, ' ', end='')
    c += 1
    sleep(1)
print('FIM')'''
print('\033[30m-\033[m'*30,'30')
print('\033[31m-\033[m'*30,'31')
print('\033[32m-\033[m'*30,'32')
print('\033[33m-\033[m'*30,'33')
print('\033[34m-\033[m'*30,'34')
print('\033[35m-\033[m'*30,'35')
print('\033[36m-\033[m'*30,'36')
print('\033[37m-\033[m'*30,'37')
