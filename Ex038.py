a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

if a>b:
    print('O maior número é o primeiro que vale {}'.format(a))
elif b>a:
    print('O maior número é o segundo que vale {}'.format(b))
else:
    print('Não existe número maior por que os dois números são iguais')
print('FIM')