p = ('aprender','programar', 'linguagem', 'python', 'curso', 'gratis', 'estedar', 'praticar', 'trabalhar', 'mercado',
     'programador', 'mercado', 'programador', 'futuro')
for n in p:
    print(f'\nNa palavra {n.upper()}, temos: ', end='')
    for l in n:
        if l.lower() in 'aeiouy':
            print(l, end=' ')