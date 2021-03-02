l = list()
lp = list()
li = list()
while True:
    a = int(input('Digite um número: '))
    l.append(a)
    r = str(input('Gostaria de continuar S/N? ')).upper().strip()
    while r not in 'SN':
        r = str(input('kkGostaria de continuar S/N? ')).upper().strip()
    if r in 'Nn':
        break
for a in l:
    if a % 2 == 0:
        lp.append(a)
    else:
        li.append(a)
print(f'A lista digita é {l}.', f'\nA lista com números pares é {lp}.', f'\nA lista com números inpares é {li}.', '\nFIM')
