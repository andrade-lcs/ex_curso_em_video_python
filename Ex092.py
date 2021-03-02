from time import sleep
import datetime
l = dict()
l['Nome'] = str(input('Nome: ')).title().strip()
a = datetime.date.today().year - int(input('Nascimento: '))
l['Idade'] = a
l['CTPS'] = int(input('N. da Carteira de Trabalho: '))
if l['CTPS'] != 0:
    print('-'*30)
    b = int(input('Ano de contratação: '))
    l['Contratação'] = b
    l['Salário'] = float(input('Salário: R$'))
    #ap = 35 - (datetime.date.today().year - b) + datetime.date.today().year
    ap = 35 + b
    if a >= 65:
        ap = ('Aposentado por idade')
        l['Aposentadoria'] = ap
    elif ap <= datetime.date.today().year:
        ap = ('Aposentado por contribuição')
        l['Aposentadoria'] = ap
    else:
        ap = 35 + b
        l['Aposentadoria'] = ap
else:
    l['CTPS'] = str('Pessoa ainda não cadastrada')
print('-'*30)
for c, n in l.items():
    print(f'O {c} tem o valor de \033[034m{n}\033[m.')
    sleep(1)
sleep(1)
print('-'*30)
sleep(2)
print(f'{"FIM":^30}')
sleep(2)
print('-'*30)
