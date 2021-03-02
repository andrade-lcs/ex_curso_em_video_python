import math
import random

print('O software vai escolher dois números')
a = random.uniform(1,100)
b = random.uniform(1,100)
print('Os números escolhidos foram {:.2f} e {:.2f}.'.format(a,b))
c = math.hypot(a,b)
print('A hipotenusa entre os catetos {:.2f} e {:.2f} é {:.2f}'.format(a,b,c))
