def j(abc):
    print('-'*30)
    print(abc)
    print('-'*30)


j(str(input('João quer queijo')))

'''def s(a, b):
    s = a + b
    print(s)


s(5, 8)
s(100, -50)
s(-5, - 8)'''

def c(* num):
    #print(num)
    for v in num:
       print(f'{v} ', end='')
    #print('FIM')
    t=len(num)
    print(f'Recebi {num} e são ao todos {t}.')


c(2, 1, 3)
c(8, 0)
c(7, 9, 4, 4, 8, 0)


'''def d(l):
    p = 0
    while p < len(l):
        l[p] *=2
        p +=1


v = [6, 3, 9, 1, 0, 2]
print(v)
d(v)
print(v)'''


'''def soma(*v):
    s = 0
    for n in v:
        s += n
    print(f'A soma dos valores {v} é {s}')


soma(5, 2)
soma(2, 9, 4)
soma(0, -2, 4)'''