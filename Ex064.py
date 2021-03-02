a = 0
s = 0
c = 0
while a != 999:
    a = int(input('Digite um número: [ou 999 para parar] '))
    if a == 999:
        break
    c = c + 1
    s = a + s
print(f'A soma dos {c} termos que você digitou é {a}.')
