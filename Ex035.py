print('Digite o comprimento de uma reta:')
a = int(input())
print('Digite o comprimento de outra reta:')
b = int(input())
print('Digite o comprimento de mais uma reta:')
c = int(input())
if a<b+c and b<a+c and c<a+b:
    print('os segmenots {}, {} e {} podem formar um triângulo.'.format(a, b, c))
else:
    print('Os segmentos {}, {} e {} NÃO podem formar um triângulo.'.format(a, b, c))
print('_' * 10, "FIM", '_' * 10)