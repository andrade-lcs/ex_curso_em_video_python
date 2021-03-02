from time import sleep
from random import randint
from operator import itemgetter
j = dict()
l = list()
r = str(input('Gostaria de inicia o jogo S/N:')).upper().strip()
while r not in 'SN':
    r = str(input('Gostaria de inicia o jogo S/N:')).upper().strip()
while r == 'S':
    for c in range(1, 5):
        j['Jogador'] = c
        j['resultado'] = int(randint(1, 6))
        l.append(j.copy())
    print(l)
    for k, n in enumerate(l):
        for c in n.items():
            print(f'{c} tirou {n.values()} no dado.')
            sleep(1)
    r = str(input('Gostaria de continuar S/N: ')).upper().strip()
    while r not in 'SN':
        r = str(input('Gostaria de continuar S/N: ')).upper().strip()
    l.clear()
    j.clear()
    print('-' * 49)
    if r == 'N':
        sleep(1)
        break
print(f'{"FIM":^49}')

'''print('Vamos jogar?\nAperte ENTRE!!!')
sleep(1)
print('-'*20)
sleep(1)
j = {'Jogador_1': randint(1, 6),
     'Jogador_2': randint(1, 6),
     'Jogador_3': randint(1, 6),
     'Jogador_4': randint(1, 6)}
r = {}
for k, v in j.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-'*20)
sleep(1)
r = sorted(j.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(r):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('-'*20)
sleep(1)
print('FIM')'''

