print('Vamos calcular uma progressão aritmétrica!')
a = int(input('Digite o primeiro termo: '))
b = int(input('Digite a razão da sua PA: '))
print('Estes são os 10 primeiros termos da sua PA:')
c = 1
e = 10
while c < e:
    d = a+(c-1)*b
    print('{}, '.format(d),end='')
    c = c+1
while e != 0:
    e = int(input('\n\nVocê quer mais quantos termos: '))
    f = c + e
    while c < f:
        d = a + (c - 1) * b
        print('{}, '.format(d), end='')
        c = c + 1