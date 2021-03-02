'''def fatorial(num=0):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


#n = int(input('Digite um número: '))
#print(f'O fatorial do número {n} é {fatorial(n)}.')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f1, f2, f3)
print('FIM')'''
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


v = int(input('Digite um númeor'))
print(par(v))