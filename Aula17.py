#n = [2, 5, 9, 1]
#n[2] = 3
#n.append(7)
#n.sort()
#n.sort(reverse=True)
#n.insert(2, 2')
#print(n)
#n.pop(2)
#n.remove(2)
#if 4 in n:
#    n.remove(4)
#else:
#    print('numero 4 não encontrado')
#print(n)
#print(f'Essa lista tem {len(n)} elementos')

#v = list()
#v = []
#v.append(5)
#v.append(9)
#v.append(4)
#for c in range(0, 5):
#    v.append(int(input('Digite um valor')))
#for c, vv in enumerate(v):
#    print(f'Na posição {c+1} encontrei o valor {vv}...')
#print('Final da lista')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')