l = list()
a = int(input('Digite a quantidade de valores que você deseja: '))
print('-'*20)
for c in range(0, a):
    l.append(int(input('Digite um valor: ')))
#print(l)
ma = me = l[1]
for cc, v in enumerate(l):
    if v > ma:
        ma = v
    if v < me:
        me = v
print(f'O maior valor é {ma} na posição ', end='')
for i, v in enumerate(l):
    if ma == v:
        print(f'{i+1}', end=' ')
print(f'\nO menor valor é {me} na posição ', end='')
for i, v in enumerate(l):
    if me == v:
        print(f'{i+1}', end='')
