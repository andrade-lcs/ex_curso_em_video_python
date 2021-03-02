nome = str(input('Qual é o seu nome:\n'))
if nome=='Gustavo':
    print('Que nome bonito')
elif nome in 'João Pedro Jose':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!.'.format(nome))
print('FIM')