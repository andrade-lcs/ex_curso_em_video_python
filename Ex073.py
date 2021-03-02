from time import sleep
times = ('Atlético-MG', 'Atlético-PR', 'Avaí-SC', 'Bahia-BA', 'Botafogo-RJ', 'Ceará-CE', 'Chapecoense-SC',
         'Corinthians-SP', 'Cruzeiro-MG', 'CSA-AL', 'Flamengo-RJ', 'Fluminense-RJ', 'Fortaleza-CE', 'Goiás-GO',
         'Grêmio-RS', 'Internacional-RS', 'Palmeiras-SP', 'Santos-SP', 'São Paulo-SP', 'Vasco-RJ')
print('-='*20)
for t in times:
    print(t)
    sleep(.25)
print('-='*20)
print(f'O campeonato brasileiro possui {len(times)} times')
sleep(2)
print('-='*20)
print(f'Os 5 primeiros classificados são: {(times[:5])}')
sleep(2)
print('-='*20)
print(f'Os quatro últimos classificados são: {(times[-4:])}')
sleep(2)
print('-='*20)
print(f'Os times do campeonato brasileiro são: {sorted(times)}')
sleep(2)
print('-='*20)
print(f'O Goiás está na {times.index("Goiás-GO")+1}ª colocação.')