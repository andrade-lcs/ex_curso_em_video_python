from random import randint
from time import sleep
l = list()
print('-'*30)
print(' '*8, 'Mega Sena', ' '*8)
print('-'*30)
a = int(input('Quantos jogos você gostaria de registrar? '))
sleep(1)
print('='*30)
for c in range(0, a):
    sleep(1)
    print(f'{c+1}º Jogo:',end='')
    for i in range(0, 6):
        n = randint(1, 60)
        while n in l:
            n = randint(1, 60)
        l.append(n)
    print(l)
    l.clear()
sleep(5)
print('\n','<'*9, 'Boa-sorte','>'*9)