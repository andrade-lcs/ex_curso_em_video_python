l = []
p = 0
for c in range(0, 5):
    a = int(input('Digiet um número: '))
    if c == 0 or a > l[-1]:
        l.append(a)
        print(f'O número {a} foi adicionado na posição {len(l)-1}')
    else:
        while p < len(l):
            if a <= l[p]:
                l.insert(p, a)
                print(f'O número {a} foi adicionado na posição {p}')
                break
            p += 1
print(f'A lista digitada foi {l}')