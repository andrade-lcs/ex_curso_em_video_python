a = str(input('Digite seu nome completo: ')).lower(). strip()
aa = a.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(aa[0].title()))
print('Seu último nome é {}.'.format(aa[-1].title()))
