j = dict()
g = list()
s = 0
j['Nome'] = str(input('Nome do Jogador: '))
j['Jogos'] = int(input(f'Quantos jogos o {j["Nome"]} jogou na temporada: '))
for n in range(1, j['Jogos']+1):
    a = int(input(f'Quantos gols na partida {n}? '))
    g.append(a)
    s += a
j['Gols'] = g
j['Total'] = s
print('-'*30)
print(j)
print('-'*30)
for c, i in j.items():
    print(f'No campo {c} tem o valor {i}.')
print('-'*30)
print(f'O jogador {j["Nome"]} jogou {j["Jogos"]} partidas.')
for k, v in enumerate(g):
    print(f'Na {k+1}º partida, fez {v} gols.')
print(f'Na temporada fez {j["Total"]} gols.')
print('-'*30)
