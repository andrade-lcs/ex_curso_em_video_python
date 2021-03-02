def j(*n, sit=False):
    '''

    :param n: digite os valores das notas dos alunos
    :param sit: escolha entre True e False para verificar a situação do aluno
    :return: sera retornado a quantidade de notas, a maior e a menor nota, a média e a situação do aluno.
    desemvolvido por Lucas Andrade
    '''
    d = dict()
    c = ma = me = s = 0
    #for v in n:
    #    c += 1
    #    if v > ma:
    #        ma = v
    #    if c == 1:
    #        me = v
    #    if v < me:
    #        me = v
    #    s += v
    #m = s/c
    #d['Total'] = c
    #d['Maior nota'] = ma
    #d['Menor nota'] = me
    #d['Média'] = m
    d['Total'] = len(n)
    d['Maior nota'] = max(n)
    d['Menos nota'] = min(n)
    d['Média'] = sum(n)/len(n)
    if sit == True:
        if d['Média'] >= 7:
            si = 'Boa'
        elif 5 <= d['Média'] < 7:
            si = 'Regular'
        else:
            si = 'Ruim'
        d['Situação'] = si
    #return f'{c}, {ma}, {me}, {m}, {si}'
    return f'{d}'


resp = j(5.5, 2.5, 0, 6.5, sit=True)
print(resp)