from math import trunc
b = int(input('Digite um número: '))
s = 0
for n in range(1, b+1, 2):
    a = n/3
    if a == trunc(a):
        print(n)
        s += n
print('A soma dos número impares multiplos de 3 de 0 a {} é {}.'.format(b, s))
print('FIM')
