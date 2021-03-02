#from math import factorial
a = int(input(('Digite um número: ')))
c = a
f = 1
print('O fatorial de {}, é:'.format(a))
print('{}! = '.format(a),end='')
for c in range(a,0,-1):
    print('{}'.format((c)), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f *c
print(f)