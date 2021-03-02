#t = list()
#t.append('Lucas')
#t.append(29)
#p = list()
#p.append(t[:])
#t[0] = 'Maria'
#t[1] = 22
#p.append(t[:])
#print(t)
#print(p)
p =[['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(p[0])
print(p[0][0])
print(p[2][1])
print(p[-1][-1])
for i in p:
#    print(i[0])
    print(f'{i[0]} tem {i[1]} anos de idade.')
'''
g = list()
d = list()
tme = tma = 0
for c in range(0, 3):
    d.append(str(input('Nome: ')).title().strip())
    d.append(int(input('Idade: ')))
    d.append(str(input('Sexo [F/M]')).upper().strip())
    g.append(d[:])
    d.clear()
print(g)
for p in g:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        tma += 1
    else:
        print(f'{p[0]} é menor de idade.')
        tme += 1
print(f'Temos {tma} pessoas maiores de idade.\nTemos {tme} pessoas menores de idade.\nFIM')'''