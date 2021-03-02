p = {'nome': 'Lucas', 'sexo': 'M', 'idade': 22}
#print(p['idade'])
#print(f'O {p["nome"]} tem {p["idade"]} anos')
#print(p.keys())
#print(p.values())
#print(p.items())
for k in p.keys():
    print(k)

for v in p.values():
    print(v)
for k, v in p.items():
    print(f'{k} = {v}')
#del p['sexo']
#p['nome'] = 'Bruna'
#p['peso'] = 85.1
#for k, v in p.items():
#    print(f'{k} = {v}')'''
#es1 = {'uf': 'Rio de Janeiro', 's': 'RJ'}
#es2 = {'uf': 'São Paulo', 's': 'SP'}
#p = []
#p.append(es1)
#p.append(es2)
#print(es2)
#print(p)
#print(p[1])
#print(p[1]['uf'])
#es = dict()
#p = list()
#for c in range(0, 2):
#    es['uf'] = str(input('Unidade federativa: ')).title().strip()
#    es['sigla'] = str(input('Sigla do estado: ')).upper().strip()
#    p.append(es.copy())
#print(p)
#for e in p:
#    print(e)
#for e in p:
#    for k, v in e.items():
#        print(f'O campo {k} tem o valor {v}.')
#    for v in e.values():
#        print(v, end='-')
#