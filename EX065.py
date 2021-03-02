r = 'S'
c = 0
s = 0
ma = 0
me = 100000000000000
while r == 'S':
    a = int(input('Digite um número: '))
    c += 1
    s += a
    if a > ma:
        ma = a
    if a < me:
        me = a
    r = str(input('Digite "S" se continuar e "N" se deseja sair: ')).upper()
print('Você digitou {} números, a média é {}, o maior número é {} e o menor númeor é {}.'.format(c, s/c, ma, me))