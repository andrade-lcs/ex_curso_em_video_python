a = 1
c = s = 0
while a != 999:
    a = int(input('Digite um valor: [ou 999 para parar]'))
    if a == 999:
        break
    c += 1
    s += a

print(f'Foram digitados {c} e a soma entre eles é {s}.')
