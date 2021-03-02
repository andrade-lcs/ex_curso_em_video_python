from datetime import date

me = 0
ma = 0
for c in range(1, 8):
    n = int(input('Digite a data de nascimento: '))
    if date.today().year - n < 18:
        me = me + 1
    else:
        ma = ma + 1
print('No grupo de pessoas digitadas {} são menores de idade e {} são maiores de idade.'.format(me, ma))
print('FIM')
