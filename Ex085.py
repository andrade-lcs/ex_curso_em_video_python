l = list()
lp = list()
li = list()
l.append(lp)
l.append(li)
for c in range(1, 8):
    a = int(input('Digite um número: '))
    if a % 2 == 0:
        lp.append(a)
    else:
        li.append(a)
sorted(l)
print(f'Os números pares são {lp})')
print(f'Os números impares são {li}')
print(l)
