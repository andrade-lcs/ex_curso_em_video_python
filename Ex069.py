print('\033[35;40m-\033[m'*30)
r = str('S')
a = str('Cadastro de pessoa')
c = ci = ch = cm = 0
while r != 'N':
    print(f'{a:-^30}')
    print('\033[35;40m-\033[m'*30)
    n = str(input('Digite o nome da pessoa: ')).title()
    i = int(input('Digite a idade da pessoa: '))
    while i < 0 or i > 150:
        print('\033[41mOpção invalida.\033[m')
        i = int(input('Digite a idade da pessoa: '))
    s = str(input('Digite F para o \033[31m[sexo feminino]\033[m ou M para o \033[34m[sexo masculino]\033[m: ')).upper().strip()
    while s not in 'FfMn':
        print('\033[41mOpção invalida.\033[m')
        s = str(input('Digite F para o \033[31m[sexo feminino]\033[m ou M para o \033[34m[sexo masculino]\033[m: ')).upper().strip()
    c += 1
    r = str(input('Deseja continuar: S/N')).upper().strip()
    if i < 18:
        ci += 1
    if s == 'M':
        ch += 1
    if s == 'F' and i < 20:
        cm += 1
print(f'Você cadastrou {c} pessoas.\n{ci} são menores de idade.\n{ch} são homens.\n{cm} são mulheres com menos de 20 anos.')
print('\033[35;40m-\033[m'*12,'FIM','\033[35;40m-\033[m'*12)