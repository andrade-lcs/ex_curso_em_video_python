s = 0
#from math import trunc
for a in range(0, 6):
    b=int(input('Digite um número: '))
    #if b/2 == trunc(b/2):
    if b % 2 == 0:
        s=s+b
print('A soma dos números pares digitados é {}'.format(s))
print('FIM')