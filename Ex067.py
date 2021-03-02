from time import sleep
print('\033[2;35;40m-=\033[m'*20)
a = int(input('Você quer ver a tabuada de qual valor? '))
while a > 0:
    n = 1
    print('\033[2;35;40m-=\033[m'*20)
    print(f'A tabuada do valor {a} é:')
    for n in range(n, 11, 1):
        print(f'{a} x {n} = {a*n}')
        sleep(.25)
        if n == 10:
            break
    sleep(1)
    print('\033[2;35;40m-=\033[m'*20)
    a = int(input('Você quer ver a tabuada de qual valor? '))
print('\033[2;35;40m-=\033[m' * 15, '\nNão calculamos a tabuada para números negativos.\nInicie o software novamente.')