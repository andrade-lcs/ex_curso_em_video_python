a = int(input('Digite um número inteiro: '))
b = 0
for c in (1, 0, 1):
    if a//c == 0:
        b = b + 1
if b == 2:
    print('O número {} é um número primo.'.format(a))
else:
    print('O número {} não é um número primo.'.format(a))
print('-='*5,'FIM','-='*5)