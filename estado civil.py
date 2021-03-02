lista = ('casada', 'solteira', 'separada', 'viuva')
p_cas = 0
p_sol = 0
p_sep = 0
p_viu = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade == 0:
        break
    est_civ = input('Digite o estado civil: ').strip().lower()
    while est_civ not in lista:
        print('\033[31mEstado civil errado, digite um estado civil válido.\033[m')
        est_civ = input('Digite o estado civil: ')
        if est_civ in lista:
            break
    if est_civ == 'casada':
        print('pessoa casada salva')
        p_cas += 1
    elif est_civ == 'solteira':
        print('pessoa solteira salva')
        p_sol += 1
    elif est_civ == 'separada':
        print('pessoa separada salva')
        p_sep += 1
    else:
        print('pessoa viúva salva')
        p_viu += 1

print(f'Foram adicionadas {p_cas} pessoas casadas')
print(f'Foram adicionadas {p_sol} pessoas solteiras')
print(f'Foram adicionadas {p_sep} pessoas separadas')
print(f'Foram adicionadas {p_viu} pessoas viúva')
