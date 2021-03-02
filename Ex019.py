#import random
from random import choice
a = str(input('Digite o nome de um aluno: '))
b = str(input('Digiete o nome de outro aluno: '))
c = str(input('Digiete o nome de outro aluno: '))
d = str(input('Digiete o nome de outro aluno: '))
l = [a,b,c,d]
print('O Software vai escolher um dos alunos para apagar o quadro')

#e = str(random.choice(l))
e = str(choice(l))
print('O aluno escolhido foi {}'.format(e))

