from time import sleep
j = dict()
g = list()
l = list()
r = 'S'
t = 0
while True:
    s = 0
    j['Num.'] = t
    t += 1
    j['Nome'] = str(input('Nome do Jogador: ')).title().strip()
    j['Jogos'] = int(input(f'Quantos jogos o {j["Nome"]} jogou na temporada: '))
    for n in range(1, j['Jogos'] + 1):
        a = int(input(f'Quantos gols na partida {n}? '))
        g.append(a)
        s += a
    j['Gols'] = g[:]
    j['Total'] = s
    l.append(j.copy())
    g.clear()
    r = str(input('Gostaria de continuar S/N: ')).upper().strip()
    while r not in 'SN':
        r = str(input('Gostaria de continuar S/N: ')).upper().strip()
    print('-' * 49)
    if r == 'N':
        sleep(1)
        break
for v in j.keys():
    print(f'{v:^15}', end='|')
print()
for c, i in enumerate(l):
    sleep(1)
    for k in i.values():
        print(f'{str(k):^15}', end='|')
    print()
while True:
    sleep(1)
    print('-'*50)
    print(('Gostaria de ver os dados de qual jogador:\n(ou aperte 999 para finalizar)'))
    r = int(input(''))
    sleep(1)
    if r == 999:
        break
    elif r >= len(l) or r < 0:
        print(f'{"-"*10}{"Número inváldo":^20}{"-"*10}')
        sleep(1)
        print()
    else:
        print('Procurando...')
        sleep(1)
        for w, q in enumerate(l[r]['Gols']):
            print(f'No jogo {w} fez {q} gols.')#resposta
            sleep(1)
            #if r == w+1: #proposta mais completa
            #    print(f'O jogador {q["Nome"]} jogou {q["Jogos"]} partidas e fez {q["Total"]} gols na temporada.\n'
            #          f'Sendo os gols {q["Gols"]}.')
print((f'{"FIM":^50}'))
