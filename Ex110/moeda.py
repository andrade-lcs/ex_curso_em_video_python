def aumentar(preço=0, taxa=0, formato=True):
    res = preço + (preço*taxa)/100
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=True):
    res = preço - (preço*taxa)/100
    return res if formato is False else moeda(res)


def multiplicar(preço=0, razão=2, formato=True):
    res = preço*razão
    return res if formato is False else moeda(res)


def dividir(preço=0, razão=2, formato=True):
    res = preço/razão
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxad=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado \t{moeda(preço)}')
    print(f'{taxaa}% de aumento \t\t{aumentar(preço, taxaa)}')
    print(f'{taxad}% de diminuição \t{diminuir(preço, taxad)}')
    print(f'O dobro do preço é \t{multiplicar(preço)}')
    print(f'A metade do preço é {dividir(preço)}')
    print('-*30')
