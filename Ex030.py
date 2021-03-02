from random import randint
g = 1
while g == 1:

    a = int(input('Você gostaria de escolher um número? Digite [ 1 ] para SIM e [ 0 ] para NÃO: '))
    if a == 0:
        print('O software vai escolher um número')
        b = randint(0, 10)
        print('O número escolhido foi: {}'.format(b))
        c = b % 2
        if c == 0:
            print('O número escolhido é PAR')
        else:
            print('O número escolhido é IMPAR')
    else:
        b = int(input('Digite um número: '))
        c = b % 2
        if c == 0:
            print('O número escolhido é par')
        else:
            print('O número escolhido é impar')
    print(' ')
    g = int(input('Você gostaria de contiuar? Digite [ 1 ] para SIM e [ 0 ] para NÃO: '))
print('FIM')