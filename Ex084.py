from time import sleep
r = 0
c = pma = 0
pme = 10000
p = list()
l = list()
lpma = list()
lpme = list()
while True:
    p.append(str(input('Nome: ')).title().strip())
    p.append(int(input('Peso: ')))
    l.append(p[:])
    p.clear()
    c += 1
    r = str(input('Gostaria de continuar [S/N]? ')).upper().strip()
    while r not in 'SN':
        r = str(input('Gostaria de continuar [S/N]? ')).upper().strip()
    if r == 'N':
        break
#print(l)
for i in l:
    if i[1] > pma:
        lpma.clear()
        pma = i[1]
        lpma.append(i)
    if i[1] == pma:
        lpma.append(i)
    if i[1] < pme:
        lpme.clear()
        pme = i[1]
        lpme.append(i)
    if i[1] == pme:
        lpme.append(i)
sleep(.5)
print(f'Foram cadastradas {c} pessoas.')
sleep(.5)
print(f'O maior peso é {lpma[0][1]}kg do(s) {lpma[0][0]}')
sleep(.5)
print(f'O menor peso é {lpme[0][1]}kg do(s) {lpme[0][0]}')
print(lpma)
print(lpme)
