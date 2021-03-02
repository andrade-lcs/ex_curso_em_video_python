print('Vamos calcular uma progressão aritmétrica!')
a = int(input('Digite o primeiro termo: '))
b = int(input('Digite a razão da sua PA: '))
print('Estes são os 10 primeiros termos da sua PA:')
for c in range(1, 11):
    d = a+(c-1)*b
    print('{}'.format(d))