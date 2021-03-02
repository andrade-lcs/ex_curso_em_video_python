n = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
    'Quinze', ' Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
#a = int(input('Digite um número entre 1 e 20: '))
#if a <= 0 or a > 20:
#    a = int(input('Digite um número entre 1 e 20: '))
r = 'S'
while r == 'S':
    while True:
        a = int(input('Digite um número entre 1 e 20: '))
        if 0< a <=20:
            break
        print('Tente novamente.')
    print(n[a - 1])
    r = str(input('Gostaria de começar novemente? S/N')).upper().strip()
    while r not in 'SN':
        r = str(input('Gostaria de começar novemente? S/N')).upper().strip()
