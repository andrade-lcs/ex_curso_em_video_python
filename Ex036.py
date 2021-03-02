from time import sleep
aa = 0
print('\033[2;31;40m-=\033[m'*40)
while aa == 0:
    print('Este software ira calcular seu financiamento')
    sleep(1)
    a = float(input('Qual é a sua renda mensal? R$'))
    sleep(1)
    b = float(input('Qual é o valor do imóvel? R$'))
    sleep(1)
    c = float(input('Em quantos anos deseja efetuar o pagamento? '))
    sleep(1)
    print('\33[2;31;40m-=\33[m'*40,'\nAguarde os calsulos')
    p = b/(c*12)

    if p < a*0.3:
        sleep(1)
        print('\33[2;31;40m-=\33[m'*40,)
        print('\nPARABÉNS!!!\nVocê teve seu financiamento aprovado!\nO imóvel de valor R${:.2f} será financiado em {:.0f} anos com prestações de R${:.2f}.\n\n\n'.format(b, c, p))
        aa = 1
        sleep(2)
    else:
        sleep(1)
        print('\33[2;31;40m-=\33[m' * 40, '\nAguarde os calsulos')
        print('Me desculpe, mas o seu fianciamento não foi altorizado.\nTente diminuir o valor fianciado ou aumentar o prazo de financiamento.\n')
        sleep(2)
        print('\33[2;31;40m-=\33[m'*40,)
        aa = int(input('Digige 0 para tentar novamente ou 1 para sair\n'))
print('\33[2;31;40m-=\33[m'*40,'\nFIM')