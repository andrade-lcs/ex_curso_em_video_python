def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mSoftware interrompido pelo usuário.\033[m')
            break
        except(ValueError, TypeError):
            print('\033[31mERRO!, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (KeyboardInterrupt):
            print('\033[31mSoftware interrompido pelo usuário.\033[m')
            break
        except(ValueError, TypeError):
            print('\033[31mERRO!, digite um número inteiro válido.\033[m')
            continue
        else:
            return n

n1 = leiaint('Digite um valor inteiro: ')
n2 = leiafloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1}')
print(f'O valor real digitado foi {n2:.2f}')
print('FIM'.center(30))
