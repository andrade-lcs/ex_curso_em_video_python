from time import sleep
l = list()
print('-'*30)
print(f'{"CALCULO DE NOTAS":>22}')
while True:
    print('-'*30)
    n = str(input('Digite o nome do aluno:')).title().strip()
    n1 = float(input('1º Nota: '))
    n2 = float(input('1º Nota: '))
    m = (n2 + n1) / 2
    l.append([n, [n1, n2], m])
    r = str(input('Gostaria de continuar S/N: ')).upper().strip()
    while r not in 'SN':
        r = str(input('Gostaria de continuar S/N: ')).upper().strip()
    if r == 'N':
        sleep(1)
        break
print('-'*30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
for i, a in enumerate(l):
    sleep(.5)
    if a[2] >= 6:
        print(f'{i:<4}{a[0]:<10}\033[034m{a[2]:>8.1f}\033[m')
    else:
        print(f'{i:<4}{a[0]:<10}\033[031m{a[2]:>8.1f}\033[m')
print('-'*30)
sleep(3)
t = int(input('Gostaria de vizualizar a nota de algum aluno?\n'
               '[Digite o número do aluno ou (999) para sair] ' ))
while t != 999:
    for i, a in enumerate(l):
        if t == i:
            print('-' * 30)
            print(f'{"No.":<4}{"Nome":<10}{"Notas":>8}')
            print(f'{i<4}{a[0]:<10}{a[1][0]:>4.1f}{a[1][1]:>4.1f}')
    sleep(1)
    t = int(input('Gostaria de vizualizar a nota de algum aluno?\n'
                   '[digite o número do aluno ou 999 para sair] '))
    if t == 999:
        break
print('-'*30)
sleep(2)
print(f'{"Programa encerrado":>22}')
print('-'*30)
