from time import sleep
from random import randint
b = dict()
t = list()
c = 1
print('-'*49)
print(f'{"Boletim":^49}')
print('-'*49)
while True:
    b['Posição'] = c
    c += 1
    b['Nome'] = str(input('Nome: ').title().strip())
    b['Média'] = float(randint(4, 10))
    print(f'Média: {b["Média"]}')
    me = b['Média']
    if me >= 6.0:
        b['Resultado'] = 'Aprovado'
    else:
        b['Resultado'] = 'Reprovado'
    t.append(b.copy())
    r = str(input('Gostaria de continuar S/N: ')).upper().strip()
    while r not in 'SN':
        r = str(input('Gostaria de continuar S/N: ')).upper().strip()
    print('-' * 49)
    if r == 'N':
        sleep(1)
        break
print('', end='|')
for i in b.keys():
    print(f'{i:^11}', end='|')
sleep(1)
for c in t:
    print('')
    print('', end='|')
    for v in c.values():
        if v == 'Reprovado':
            print(f'\033[031m{v:^11}\033[m', end='|')
        elif v == 'Aprovado':
            print(f'\033[034m{v:^11}\033[m', end='|')
        else:
            print(f'{v:^11}', end='|')
    sleep(1)
print('')
print('-'*49)
sleep(3)
print(f'{"FIM":^49}')
print('-'*49)