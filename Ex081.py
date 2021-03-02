l = list()
a = int(input('Digite quantos valores você deseja digitar: '))
for c in range(0, a):
    v = int(input('Digite um valor: '))
    l.append(v)
print(f'Foram adicionados {len(l)} números a lista.')
l.sort(reverse=True)
print(f"A lista criada é {l}")
if 5 in l:
    print(f'O valor 5 foi acrescentado na posição {l.index(5)+1}')
else:
    print('O valor 5 não foi acrescentado na lista')
print('FIM')
