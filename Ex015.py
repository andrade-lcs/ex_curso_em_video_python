d = int(input('Quantos dias alugaram o carro? '))
q = float(input('Quantos quilometros foram percorridos?'))
pd = 60
pq = 0.15
print('O aluguel do carro de {} dias, que percorreu a distância de {}Km, resultou em um preço de R${:.2f}'.format(d,q,d*pd+q*pq))
