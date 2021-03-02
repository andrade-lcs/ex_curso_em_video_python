import math
import random

n = float(random.uniform(-100,100))
print('O software vai excolher um número')
print('O número escolhido é {:.2f}'.format(n))
m = int(math.trunc(n))
print('A parte inteira do número é {:.0f}'.format(m))
