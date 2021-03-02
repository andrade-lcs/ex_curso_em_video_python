#import random
#from random import sample
from random import shuffle
a = str(input('Digite o nome de um aluno: '))
b = str(input('Digiete o nome de outro aluno: '))
c = str(input('Digiete o nome de outro aluno: '))
d = str(input('Digiete o nome de outro aluno: '))
l = [a, b, c, d]
print('O Software vai escolher a order de apresentação dos trabalhos')

#e = str(random.sample(l,4))
#e = str(sample(l,4))
shuffle(l)
print('A ordem determinada é:',l)
