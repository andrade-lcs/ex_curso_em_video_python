print('Digite um número:')
a = int(input())
print('Digite outro número')
b = int(input())
print('Digite mais um número')
c = int(input())
if a > b and a > c:
    print('O maior valor é {}.'.format(a))
if b > a and b > c:
    print('O maior valor é {}.'.format(b))
if c > a and c > b:
    print('O maios valor é {}.'.format(c))
if a < b and a < c:
    print('O menor valor é {}.'.format(a))
if b < a and b < c:
    print('O menor valor é {}.'.format(b))
if c < a and c < b:
    print('O menor valor é {}.'.format(c))
print('FIM')