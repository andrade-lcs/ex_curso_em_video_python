num = int(input('Digite um número: '))
soma = 0
c = 0
lista = []
while num*num != soma:
    c += 1
    if c % 2 != 0:
        soma += c
        lista.append(c)

print(f'{num}² = {soma} = ', end='')
for t in lista[:-1]:
    print(f'{t} + ', end='')
for t in lista[-1:]:
    print(f'{t}')