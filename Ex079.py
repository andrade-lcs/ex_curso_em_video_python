l = list()
l.append(int(input('Digite um número: ')))
r = str(input('Gostaria de digitar um número S/N: ')).upper().strip()
ma = me = 1
while r not in 'SN':
    r = str(input('Gostaria de digitar um número S/N: ')).upper().strip()
while r == 'S':
    a = int(input('Digite um número: '))
    if a not in l:
        l.append(a)
    else:
        print('Númeto já digitado.\nTente novamente')
        a = int(input('Digite um número: '))
        while a in l:
            print('Númeto já digitado.\nTente novamente')
            a = int(input('Digite um número: '))
        l.append(a)
    r = str(input('Gostaria de digitar um número S/N: ')).upper().strip()
    while r not in 'SN':
        r = str(input('Gostaria de digitar um número S/N: ')).upper().strip()
#for c in enumerate(l):
l.sort()
print(f'O maior número digitado é {l}')
print('FIM')