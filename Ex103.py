def lista(nome='<Desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} na temporada')


n = str(input('Digite o nome do jogador: ')).title().strip()
g = str(input('digite quantos gols: ')).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    lista(gols=g)
else:
    lista(n, g)
print('FIM')