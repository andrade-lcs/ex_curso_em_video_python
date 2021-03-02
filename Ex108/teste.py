from Ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'O aumento de 10% em {moeda.moeda(p)} será {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'A diminuição de 10% em {moeda.moeda(p)} será {moeda.moeda(moeda.diminuir(p, 10))}')
print(f'O dobro de {moeda.moeda(p)} será {moeda.moeda(moeda.multiplicar(p, 2))}')
print(f'A metade de {moeda.moeda(p)} será {moeda.moeda(moeda.dividir(p, 2))}')
