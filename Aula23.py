def fatorial(n):
    '''
    rotina de calculo de fatorial
    :param n: numero inteiro
    :return: resultado do fatorial
    '''
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


num = int(input('Digite um número'))
fat = fatorial(num)
print(f'o fatorial de {num} é {fat}')