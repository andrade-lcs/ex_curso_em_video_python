from random import randint
from time import sleep
print('\nPronto para jogar Pedra Patel Tesoura?\n')
a = 1
while a == 1:
    a1 = 1
    j = int(input('Quantas partidas você deseja jogar?'))
    p = 0
    while a1 < j+1:
        l = ('Pedra', 'Papel', 'Tesoura')
        b = randint(0, 2)
        print('\n{}º Rodada'.format(a1))
        c = int(input('Digite a sua escolha:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n'))
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
        sleep(1)
        print('-=' * 10, '\nComputador [{}]\nVocê [{}]\n'.format(l[b], l[c]), '-=' * 10)
        if b == c:
            print('O jogo empatou!!!')
            p = p + 0
        elif b == 0 and c == 1:
            print('VOCÊ GANHOU!!!')
            p = p + 1
        elif b == 0 and c == 2:
            print('VOCÊ PERDEU!!!')
            p = p + 0
        elif b == 1 and c == 2:
            print('VOCÊ GANHOU!!!')
            p = p + 1
        elif b == 1 and c == 0:
            print('VOCÊ PERDEU!!!')
            p = p + 0
        elif b == 2 and c == 1:
            print('VOCÊ PERDEU!!!')
            p = p + 0
        elif b == 2 and c == 0:
            print('VOCÊ GANHOU!!!')
            p = p + 1
        else:
            print('ESCOLHA INVALIDA')
        a1 = a1 + 1
    print('Você marcou {} pontos em {} partidas'.format(p, a1-1))
    if p >= a1/2:
        print('Você é um bom jogador, PARABÉNS!!!')
    else:
        print('Tente novamente.')
    a = int(input('\nDigite 1 para continuar e 0 para sair\n'))
    print('-=' * 20,'\n')
