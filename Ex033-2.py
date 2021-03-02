a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
if a > b and a > c:
    if b > c:
        print('O número {} é maior que o número {} que é melhor que o númeor {}.'. format(a, b, c))
    else:
        print('O número {} é maior que o número {} que é melhor que o númeor {}.'. format(a, c, b))
if b > a and b > c:
    if a > c:
        print('O número {} é maior que o número {} que é melhor que o númeor {}.'.format(b, a, c))
    else:
        print('O número {} é maior que o número {} que é melhor que o númeor {}.'.format(b, c, a))
if c > a and c > b:
    if a > b:
        print('O número {} é maior que o número {} que é melhor que o númeor {}.'.format(c, a, b))
    else:
        print('O número {} é maior que o número {} que é melhor que o númeor {}.'.format(c, b, a))

