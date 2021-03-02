def c(i, f, p):
    from time import sleep
    if p < 0:
        p = -p
    if p == 0:
        p = 1
    print(f'Contando de {i} até {f} de {p}.')
    if f > i:
        while i <= f:
            sleep(.25)
            print(f'{i}', end=' ')
            i += p
    elif i > f:
        while i >= f:
            sleep(.25)
            print(f'{i}', end=' ')
            i -= p
    print()
    print('-'*30)


c(1, 10, 1)
c(10, 0, 2)
print(str('Contagem personalizada'))
i = int(input('Qual o início? '))
f = int(input('Qual o fim? '))
p = int(input('Qual o incremento? '))
c(i, f, p)