a = int(input('Digite o comprimento de uma reta: '))
b = int(input('Digite o comprimento de outra reta: '))
c = int(input('Digite o comprimento de mais uma reta: '))
print(abs(b-c))
if a > abs(b-c) and a < b+c:
    print('As retas {}, {} e {} formam um triângulo.'.format(a, b, c))
if b > abs(a-c) and b < a+c:
    print('As retas {}, {} e {} formam um triângulo.'.format(a, b, c))
if c > abs(b-a) and a < b+a:
    print('As retas {}, {} e {} formam um triângulo.'.format(a, b, c))
else:
    print('As retas {}, {} e {} NÂO formam um triângulo.'.format(a, b, c))