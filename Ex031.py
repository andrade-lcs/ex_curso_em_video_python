b=1
while b==1:
    print('Qual será o distância da sua viagem em quilometros?')
    a=int(input())
    if a <=200:
        print('O custo da sua viagem será R${:.2f}.'.format(a*0.5))
    else:
        print('O custo da sua viagem será R${:.2f}'.format(a*0.45))
    print(' ')
    print('Você gostaria de calcular uma nova viagem? Digite 1 para SIM e 0 para Não')
    b=int(input())
    print(' ')
print('FIM')
