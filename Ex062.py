print('Vamos calcular uma progressão aritmétrica!')
a=int(input('Digite o primeiro termo: '))
b=int(input('Digite a razão da sua PA: '))
print('Estes são os 10 primeiros termos da sua PA:')
c=1
n=0
o=str('s')
while o in 'Ss':
    while c < 10:
        c=c+n
        d=a+(c-1)*b
        print('{}'.format(d),end='')
        print(', ' if c < 9 else '.',end='')
        c = c+1
    o=str(input('\nGostaria de continuar: S/N'))
    n=int(input('Quantos elementos a mais você quer? '))