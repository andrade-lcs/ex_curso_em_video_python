from datetime import date
a = date.today().year
b = int(input('Digite a data de nascimento do atleta: '))
i=a-b
print('A idade do atleta nascido em {} é {} anos.'.format(b,i))
if i<=9:
    print('O atleta pertence a categoria Mirim.')
elif i<=14:
    print('O atleta pertence a categoria Infantil.')
elif a-b<=19:
    print('O atleta pertence a categoria Junior.')
elif i<=20:
    print('O atleta pertence a categoria Sênior.')
else:
    print('O atleta pertence a categoria Master.')
print('FIM')