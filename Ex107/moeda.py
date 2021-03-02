def aumentar(preço, taxa=0):
    res = preço + (preço*taxa)/100
    return res


def diminuir(preço, taxa=0):
    res = preço - (preço*taxa)/100
    return res


def multiplicar(preço, razão=2):
    res = preço*razão
    return res


def dividir(preço, razão=2):
    res = preço/razão
    return res
