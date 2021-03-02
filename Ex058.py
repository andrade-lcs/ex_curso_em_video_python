from time import sleep
from random import randint
print('O computador escolheu um númeor entre 1 e 10')
a = int(randint(1, 10))
j = 1
while j < 10:
    sleep(1)
    print('-'*10, '{}º Rodada'.format(j), '-'*10)
    b = int(input('Agora você deve escolher um número entre 1 e 10: '))
    if b >10 or b <= 0:
        print('Escolha invalida')
    elif a==b:
        print('Você acertou o número que o computador escolheu em {} rodadas'.format(j))
        print('Você ganhou o jogo!')
        j = 10
    else:
        print('você escolheu o número errado')
        j = j + 1
print('Fim do jogo')