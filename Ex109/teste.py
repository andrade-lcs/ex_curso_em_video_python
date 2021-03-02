from Ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'O aumento de 10% em {p} será {moeda.aumentar(p, 10)}')
print(f'A diminuição de 10% em {moeda.moeda(p)} será {moeda.diminuir(p, 10)}')
print(f'O dobro de {moeda.moeda(p)} será {moeda.multiplicar(p, 2)}')
print(f'A metade de {moeda.moeda(p)} será {moeda.dividir(p, 2)}')
