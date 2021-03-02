a = int(input('Digite um número de 1 a 9999: '))
#b = str(a)
#print('O número digita foi {}'.format(a))
#print('Unidade {}.'.format(b[-1]))
#print('Dezena {}.'.format(b[-2]))
#print('Centena {}.'.format(b[-3]))
#print('Milhar {}.'.format(b[-4]))
u = a // 1 % 10
print('Unidade {}.'.format(u))
d = a //10 % 10
print('Dezena {}.'.format(d))
c = a //100 % 10
print('Centena {}.'.format(c))
m = a // 1000 % 10
print('Milhar {}.'.format(m))
