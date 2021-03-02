print('-='*15)
print('{:^30}'.format('Lista de compras'))
print('-='*15)
r = 'S'
pme = str()
s = pm = 0
me = 1000000000
while r == 'S':
    p = str(input('Digite o nome do produto: '))
    pp = float(input('Digite o preço do produto: R$'))
    r = str(input('Gostaria de continuar?\n[ S } sim\n[ N } não\n')).upper().strip()
    while r not in 'SN':
        print('\033[30;41mOpção incorreta\033[m')
        r = str(input('Gostaria de continuar?\n[ S } sim\n[ N } não\n')).upper().strip()
    s += pp
    if pp > 1000:
        pm += 1
    if pp < me:
        me = pp
        pme = p
print(f'Foram gastos R${s:.2f}\n{pm:.0f} produto(s) mais caros que R$1000.00.\nO produto mais barato foi {pme}\nO programa foi encerrado.')
