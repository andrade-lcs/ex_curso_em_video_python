a = str(input('Digite uma frase: ')).strip().upper()
print('A letra "a" aparece {} vezez.'.format(a.count('A')))
print('A letra "a" aparece pela primeira vez na posição {}.'.format(a.find('A')+1))
print('A última letra "a" aparece na posição {}.'.format(a.rfind('A')+1))
