a = float(input('Digite a primera nota: '))
b = float(input('Digite a segunda nota: '))
c = float(input('Digite a terceira nota:'))
d=(a+b+c)/3
if d<5:
    print('O aluno atingiu a nota {:.2f} e por isso esta reprovado.'.format(d))
elif d<6.99:
    print('O aluno atingiu a nota {:.2f} e por isso esta de recuperação.'.format(d))
else:   
    print('O aluno atingiu a nota {:.2f} e por isso esta aprovado.'.format(d))
print('FIM')