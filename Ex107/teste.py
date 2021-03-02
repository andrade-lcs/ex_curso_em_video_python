from Ex107 import moeda

p = float(input('Digite o preço: R$'))
print(f'O aumento de R${p} será R${moeda.aumentar(p, 10)}')
print(f'A diminuição de R${p} será R${moeda.diminuir(p, 10)}')
print(f'O dobro de R${p} será R${moeda.multiplicar(p, 3)}')
print(f'A metade de R${p} será R${moeda.dividir(p, 3)}')
