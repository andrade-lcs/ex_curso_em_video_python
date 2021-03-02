from time import sleep

l = list()
p = dict()
k = m = 0
while True:
    p['Nome'] = str(input('Nome: ')).title().strip()
    s = str(input('Sexo M/F: ')).upper().strip()[0]
    while s not in 'MF':
        s = str(input('Sexo M/F: ')).upper().strip()[0]
    if s == 'M':
        p['Sexo'] = 'Masculino'
    else:
        p['Sexo'] = 'Feminino'
    p['Idade'] = int(input('Idade: '))
    m = m + p['Idade']
    l.append(p.copy())
    r = str(input('Gostaria de continuar S/N: ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Gostaria de continuar S/N: ')).upper().strip()[0]
    if r == 'N':
        sleep(1)
        break
print('-'*30)
#print(l)
#for c in l:
    #k += 1
    #for n, i in c.items():
     #   print(f'O {n} ', end='')
      #  print(f'é {i} ', end='')
        #print(p.values(['Idade']))
        #if p['Sexo'] == 'Feminino':
        #    n.append(p.copy(['Sexo']))
    #print('\n')
print(f'Foram cadastrado {len(l)} pessoas')
print(f'A média de idade é {m/len(l)}.')
print(f'As mulheres da lista são ', end='')
for p in l:
    if p['Sexo'] == 'Feminino':
        print(f'{p["Nome"]} ', end='')
print()
print('As pessoas com idade acima dá média são ', end='')
for p in l:
    if p['Idade'] > (m/len(l)):
        print(f'{p["Nome"]} ', end='')
print()