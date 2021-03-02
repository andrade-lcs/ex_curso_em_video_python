a = str(input('Digite sua expressão: '))
c = 0
for s in a:
    if s == '(':
        c +=1
    elif s == ')':
         c -=1
if c == 0:
    print('Sua expressão tá correta.')
else:
    print('Sua expressão tá incorreta.')