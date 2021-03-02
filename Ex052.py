from math import trunc
a = int(input('Digite um número inteiro: '))
b = 0
for c in range(1, a):
    if a / c == trunc(a / c):
        b = b + 1
        print(c)
if b < 2:
    print('O número {}, é primo.'.format(a))
else:
    print('O número {}, não é primo.'.format(a))
print('FIM')
