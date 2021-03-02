def aumentar(preço=0, taxa=0):
    res = preço + (preço*taxa)/100
    return res


def diminuir(preço=0, taxa=0):
    res = preço - (preço*taxa)/100
    return res


def multiplicar(preço=0, razão=2):
    res = preço*razão
    return res


def dividir(preço=0, razão=2):
    res = preço/razão
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')
