#t=int(input('Quantos anos tem seu carro?'))
#if t <=3:
#   print('Carro novo')
#else:
#    print('Carro velho')
#print('Carro novo' if t<=3 else 'Carro velho')
#print('fim')
#    print('Que nome lindo')
#print('Bom dia, {}'.format(n))
#print('fim')
#_____________________________
import random
from time import sleep
c = 0
while c != 1:
    print('O computador escolherá um númeor entre 1 e 6')
    a = int(random.randint(1,6))
    b = int(input('Agora vc deve escolher um número entre 1 e 6: '))
    print('-='*20)
    sleep(2)
    if a==b:
        print('Você escolheu o número que o computador escolheu')
        print('Você ganhou o jogo!')
    else:
        print('você escolheu o número errado')
        print('O número escolhido pelo computador foi {:.0f}, e o seu {:.0f}'.format(a,b))
        print('O computador ganhou o jogo')
    print('-='*20)
    sleep(2)
    c = int(input('Para continuar digite 0 e para sair digite 1: '))
    print(' ')
print('Fim do jogo')