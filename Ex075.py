#nn = int(input('Quantos números você gostaria de digitar: '))

n = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),int(input('Digite um número: ')))
#a = int(input('Digite um número: '))
#b = int(input('Digite outro número: '))
#c = int(input('Digite mais um número: '))
#d = int(input('Digite o último número: '))
#n = (a, b, c, d)
#print(f'Você digitou os seguintes valores: {n}')
#b = int(input('Digite outro número: '))
#n = (a, b, c, d)
print(f'Você digitou os seguintes valores: {n}')
print('-='*15)
print(f'O valor 9 foi digitado {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 foi digitado na posição {n.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados são ',end='')
for num in n:
    if num % 2 ==0:
        print(f'{num}, ', end='')