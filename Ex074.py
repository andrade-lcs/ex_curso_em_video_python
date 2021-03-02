from random import randint

n = (int(randint(0, 10)), int(randint(0, 10)), int(randint(0, 10)), int(randint(0, 10)), int(randint(0, 10)))
print('Os valores sorteados são: ', end='')
for num in n:
    print(f'{num}, ', end='')
print(f'\nO maior valor sorteado foi: {max(n)}.')
print(f'O menor valor sorteado foi: {min(n)}.')
