def f(n=1, show=False):
    '''
    Esta rotina permite
    :param n: Digite o valor a se calcular o fatorial.
    :param show: Ativando esta função será detalhado as contas matemáticas.
    :return: Será o retorno na tela do usuário de acordo com os parâmetros de entrada.
    Desenvolvido por Lucas Andrade
    '''
    f=1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'1 = {f}')
    return f'O fatoria de {n} é igual a {f}.'

#help(f)
a = int(input('Digite um número: '))
b = str(input('Gostaria de ver as contas [S/N]: ')).upper().strip()[0]
if b == 'S':
    b = True
print(f(a, b))