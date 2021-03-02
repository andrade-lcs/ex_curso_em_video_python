from random import randint
from time import sleep
print('-' * 40)
print('Vamos jogar PAR ou IMPAR!!!')
p = 0
c = 1
while True:
    sleep(1)
    a = randint(0, 5)
    print('-'*15, f'{c}º Rodada', '-' * 15)
    e = str(input('Escolha PAR ou IMPAR (P/I): ')).strip().upper()[0]
    while e not in 'PpIi':
        e = str(input('Escolha PAR ou IMPAR (P/I): ')).strip().upper()[0]
    b = int(input('Escolha um número: '))
    while b < 0 or b > 10:
        b = int(input('Número invalido.\nEscolha outro número: '))
    if (a + b) % 2 == 0:
        o = str('P')
    else:
        o = str('I')
    if e == o:
        sleep(1)
        print(f'\nVocê escolheu {b} e o computador escolheu {a} total de {a + b}.')
        print('Deu PAR' if (a + b) % 2 == 0 else 'Deu IMPAR', 'e você ganhou essa partida.\n')
        p = p + 1
        c = c + 1
    else:
        sleep(1)
        print(f'\nVocê escolheu {b} e o computador escolheu {a} total de {a + b}.')
        print('Deu PAR' if (a + b) % 2 == 0 else 'Deu IMPAR', 'e você perdeu essa partida.\n')
    if e != o:
        break
print(f'Você ganhou {p} partidas.\n')
sleep(1)
print('-'*15, 'GAME OVER!', '-'*15)
