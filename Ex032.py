import datetime
b = 1
while b == 1:
    print('Digite um ano: ou digite 0 para o ano atual')
    a = int(input())
    if a == 0:
        a = datetime.date.today().year
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 :
        print('O ano {} é um ano Bissesto'.format(a))
    else:
        print('O ano {} não é um ano Bissesto'.format(a))
    print('Você gostaria de analisar outro ano?')
    print('Digite 1 para SIM e 0 para Não')
    b = int(input())
    print(' ')
print('FIM')
