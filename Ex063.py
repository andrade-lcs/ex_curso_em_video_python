print('\033[1;34;40m-=\033[m'*35)
n = int(input(('Digite quantos termos da sequênciad e Fibonacci que você quer: ')))
t1 = 0
t2 = 1
c = 3
print('{} → {}'.format(t1, t2), end='')
while c <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    c = c + 1
    t1 = t2
    t2 = t3
print('\n','\033[1;34;40m-='*15,'FIM','-='*15,'\033[m')
