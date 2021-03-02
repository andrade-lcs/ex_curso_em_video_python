print('-=' * 15)
print('{:^30}'.format('Banco do LUCAS'))
print('-=' * 15)
v = float(input('Qual valor vc deseja sacar: R$'))
t = v
c = 50
tc = 0
while True:
    if t >= c:
        t -= c
        tc += 1
    else:
        if tc > 0:
            print(f'Total de {tc} cédulas de R${c:.2f}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 5
        elif c == 5:
            c = 1
        tc = 0
        if t == 0:
            break
