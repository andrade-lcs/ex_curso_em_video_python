print('Digite a velocidade do seu carro:')
v = int(input())

if v > 80:
    m = (v-80)*7
    print('Você será multado por trafegar acima da velocidade em R${:.2f}.'.format(m))
else:
    print('Velocidade abaixo do limite permetido, BOA VIAGEM!')
print(' ')
print('Fim')