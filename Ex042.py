print('Digite o comprimento de uma reta:')
a = int(input())
print('Digite o comprimento de outra reta:')
b = int(input())
print('Digite o comprimento de mais uma reta:')
c = int(input())
if a<b+c and b<a+c and c<a+b:
    if a == b  == c:
        print('O triangulo formado pelos segmentos {}, {} e {} podem formar um triângulo Equilátero.'.format(a, b, c))
    elif a == b or a == c or b == c:
        print('O triangulo formado pelos segmentos {}, {} e {} podem formar um triângulo Isósceles.'.format(a, b, c))
    else:
        print('O triangulo formado pelos segmentos {}, {} e {} podem formar um triângulo Escaleno.'.format(a, b, c))
else:
    print('Os segmentos {}, {} e {} NÃO podem formar um triângulo.'.format(a, b, c))
print('_' * 10, "FIM", '_' * 10)