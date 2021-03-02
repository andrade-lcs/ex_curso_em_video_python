import math
import random

print('O software vai escolher um ângulo em radianos')
a = random.vonmisesvariate(0,0)
print('O ângulo excolido foi {:.2f} rad'.format(a))
cos = math.cos(a)
print('O cosseno do ângulo escolhido é {:.2f}.'.format(cos))
sen = math.sin(a)
print('O seno do ângulo escolhido é {:.2f}.'.format(sen))
tan = math.tan(a)
print('A tangente do ângulo escolhido é {:.2f}.'.format(tan))
