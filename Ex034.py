a=1
while a == 1:
    print('Digite o valor do salário do colaborador:')
    b=int(input())
    if b <=1250:
        print('O salário reajustado é R${:.2f}.'.format(b*1.15))
    else:
        print('O salário reajustado é R${:.2f}.'.format(b*1.1))
    print('Você gostaria de calcular um novo salário?')
    print('Digite 1 para SIM e 0 para Não')
    b = int(input())
    print(' ')
print('__FIM__')