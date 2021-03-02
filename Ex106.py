def linha(txt):
    '''
    Vai tomar no cu seu curioso
    :param txt:
    :return:
    '''
    c = int(len(txt)+10)
    print('\033[041m', f'-'*c)
    print(f' '*5, f'{txt}')
    print('-'*c, '\n\033[m')


def pyhelp(abc):
    linha('SISTEMA DE AJUDA PYHELP')
    print('\033[046m')
    help(a)
    print('\33[m')

while True:
    a = str(input('Escolha uma função ou biblioteca:')).strip().lower()
    if a == 'fim':
        linha('Até logo')
        break
    pyhelp(a)