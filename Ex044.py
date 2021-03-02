a=float(input('Digite o preço do produto R$: '))
b=int(input('Digite o número correspondete a forma de de pagamento:\n1 - dinheiro\n2 - cheque\n3 - a vista no cartão\n4 - '
        '2x no cartão\n5- 3x ou mais no cartão\n'))
if b == 1 or b == 2:
    print('O valor terá um desconto de 10% e custará R${:.2f}.'.format(a*0.9))
elif b == 3:
    print('O valor terá um desconto de 5% e custará R${:.2f}.'.format(a*0.95))
elif b == 4:
    print('O valor não terá desconto')
elif b == 5:
    print('O valor terá juros de 20% e custará R${:.2f}.'.format(a*1.2))
else:
    print('ERROR - opção de pagamento inexistente!')
print('FIM')