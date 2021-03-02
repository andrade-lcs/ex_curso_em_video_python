def leiainteiro(msg):
    r = False
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            n = int(n)
            r = True
        else:
            print('\033[031mERRO\033[m')
        if r:
            break
    return n


n = leiainteiro('Digite um número inteiro: ')
print(f'Você digitou o número {n}')
