l = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90,'Estojo', 25,'Transferidor', 4.2,'Compasso', 9.99, 'Mochila', 120.3)
print('-'*39, f'\n{"Listagem de preços":^39}\n'.upper(), '-'*39)

for p in range(0, len(l)):
    if p % 2 == 0:
        print(f'{l[p]:.<30}', end='')
    else:
        print(f'R${l[p]:>7.2f}')
print('-'*39)
