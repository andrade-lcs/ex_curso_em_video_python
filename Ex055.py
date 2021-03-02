ma = float()
me = float(1000000)
for c in range(1, 6):
    a =float(input('Digite o peso do pasciente: '))
    if a > ma:
        ma = a
    if a < me:
        me = a

print('O maior peso é {:.2f}Kg, e o menor peso é {:.2f}Kg.'.format(ma,me))