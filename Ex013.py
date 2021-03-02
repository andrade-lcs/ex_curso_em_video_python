n = input('Digite o nome do funcionário: ')
s = float(input('Digite o salário do funcionário: '))
r = float(input(('Digite o reajuste do funcionário em porcentagem: ')))
r1=r/100
s1=s*(1+r1)
print('O funcionário {:_^20} e receberá um salário de R${:.2f}, que representa um reajuste de {}%, um aumento de R${:.2f}.'.format(n,s1,r,s1-s))