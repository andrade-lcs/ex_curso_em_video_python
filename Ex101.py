def voto(n):
    from datetime import date
    i = (date.today().year) - n
    if i <= 1:
        return f'Com {i} ano não é permetido votar.'
    if i < 16:
        return f'Com {i} anos não é permetido votar.'
    elif 16 <= i < 18 or i > 65:
        return f'Com {i} anos o voto é facultatívo.'
    else:
        return f'Com {i} anos o voto é obrigatório.'
    #elif i < 18:
    #    return f'Com {i} anos o voto é facultatívo.'
    #elif i < 65:
    #    return f'Com {i} anos o voto é obrigatório.'
    #else:
    #    return f'Com {i} anos o voto é facultativo.'


a = int(input('Digite o ano de nascimento: '))
print(voto(a))
