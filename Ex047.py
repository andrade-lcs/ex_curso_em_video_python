from time import sleep
a = int(input('Digite um número:'))
print('-='*20, '\nOs número pares de 0 a 50 são:')
for n in range(0, a, 2):
    print(n)
    sleep(0.25)
if a % 2 == 0:
    print(a)
print('-='*5, 'FIM', '-='*5)
