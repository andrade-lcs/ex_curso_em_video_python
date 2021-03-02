from time import sleep
a = 0
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
while a != 5:
    sleep(2)
    a = int(input('MENU\n\nDigete uma opção:\n[ 1 ] - Somar\n[ 2 ] - Multiplicar\n[ 3 ] - Maior\n[ 4 ] - Novos números'
                  '\n[ 5 ] - Sair do programa\n'))
    if a <=0 or a > 5:
        print('Escolha inválida')
    elif a == 1:
        print("{} + {} = {}.".format(n1, n2, n1 + n2))
    elif a == 2:
        print("{} X {} = {}.".format(n1, n2, n1 * n2))
    elif a == 3:
        if n1 > n2:
            print('{} > {}'.format(n1, n2))
        elif n2 > n1:
            print('{} > {}'.format(n2, n1))
        else:
            print('{} = {}'.format(n1, n2))
    elif a == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
print('FIM')