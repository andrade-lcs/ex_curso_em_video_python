from time import sleep
'''def maior(*n):
    ma = -10000000000000000000000000000000000000000000
    print('Analisando valores inseridos ...')
    sleep(1)
    for v in n:
        print(v)
        if v > ma:
            ma = v
    print(f'O maior valor é digitedo é {str(maior())}')


n = list()
r = str(input('Gostaria de continuar S/N?')).upper().strip()[0]
while True:
    a = int(input('Digite um número: '))
    n.append(a)
    r = str(input('Gostaria de continuar S/N?')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Gostaria de continuar S/N?')).upper().strip()[0]
    if r == 'N':
        break
print(n)
maior(n)
print('FIM')
'''
def maior(* num):
    cont = maior = 0
    print('-'*60)
    sleep(1)
    print('Foram informados os valores ...', end='')
    for valor in num:
        print(valor, end=' ')
        sleep(.25)
        if cont == 0:
            maior = valor
        if valor > maior:
            maior = valor
        cont += 1
    print('\nAnalisando os dados ...')
    sleep(1)
    print(f'Foram informandos {cont} números ao todo, e o maior valor é {maior}.')
    sleep(1)

maior(2, 9, 4, 5, 7, 1)
#maior(4, 7, 0)
#maior(1, 2)
#maior(6)
#maior(0)
#maior(1, 2, 8, 4, -2)
#aior(-8, -7, -2, -10)
print(F'{"FIM":^60}')