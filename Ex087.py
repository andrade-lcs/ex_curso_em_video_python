from random import randint
s = t = ma = 0
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = randint(0, 100)
print('-='*15)
for l in range(0, 3):
    t += m[l][2]
    for c in range(0, 3):
        print(f'[{m[l][c]:^5}]', end='')
        if m[l][c] % 2 == 0:
            s += m[l][c]
        if m[1][c] > ma:
            ma = m[1][c]
    print()
print('-='*15)
print(f'A soma dos núemros pares é {s}')
print(f'A soma dos valores da terceira coluna é {t}')
print(f'O maior valor da segunda linha é {ma}')