while True:
    print('-'*6, 'Multiplicação', '-'*6,'\n')
    for t in range(1, 11):
        print(f'{t:2} - Tabuada do {t:2}')
    print('11 - sair')
    num = int(input('\nDigite sua opção: '))
    if num == 11:
        break
    print('-'*6, f'Tabuada do número {num}', '-'*6, '\n')
    for n in range(1, 11):
        print(f'{num:2} X {n:2} = {num*n:2}')
