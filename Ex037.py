a = int(input('Digite um número: '))
b = int(input('Digite uma das bases para conversão:\n[ 1 ] - Para converter para Binário\n[ 2 ] - Para converter para '
            'Octal\n[ 3 ] - para converter para Hexadecimal\n'))
if b == 1:
    c = bin(a)
    print('O número {} convertido para base Binária é {}.'.format(a,c[2:]))
elif b == 2:
    c = oct(a)
    print('O número {} convertido para a base Octal é {}.'.format(a,c[2:]))
elif b == 3:
    c = hex(a)
    print('O número {} convertido para a base Hexadecimal é {}.'.format(a, c[2:]))
else:
    print('ERRO - Opção invalida')