import datetime
a=datetime.date.today().year
b=int(input('Digite seu ano de nascimento: '))

if a-b<18:
    print('Você precisa se alistar em {} anos.'.format(18-(a-b)))
elif a-b==18:
    print('Você precisa se alistar ainda este ano')
else:
    print('Você não precisa se alisatar mais, pois já se passaram {} anos de seu alistamento.'.format((a-b)-18))
print('FIM')