print('Este programa calcular descontos para entrada do Zoológico')
p = 120
print('A entrada custa R%{:.2f}.'.format(p))
print('Quantas vezes vc já veio nesse Zoologico?')
a = int(input())

if a == 3:
    p = p - (a * 10)
    d = (1 - p / 120) * 100
    print('Sua entrada com desconto de %{:.2f} será R${:.2f}.'.format(d, p))
elif a == 4:
    p = p - (a * 10)
    d = (1 - p / 120) * 100
    print('Sua entrada com desconto de %{:.2f} será R${:.2f}.'.format(d, p))
elif a == 5:
    p = p - (a * 10)
    d = (1 - p / 120) * 100
    print('Sua entrada com desconto de %{:.2f} será R${:.2f}.'.format(d, p))
elif a >= 6:
    a = 6
    p = p - (a * 10)
    d = (1 - p / 120) * 100
    print('Sua entrada com desconto de %{:.2f} será R${:.2f}.'.format(d, p))
else:
    print('Sua entrada será R${:.2f}.'.format(p))

print('FIM')
