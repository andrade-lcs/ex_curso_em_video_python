i = str(input('Digite o sexo da pessoa:\n[ M ] - Masculino\n[ F ] - Feminino\n')).strip().upper()[0]
a1 = str('M')
a2 = str('F')
while i not in 'MmFf':
    print('Escolha invalida, escolha novamente.')
    i = str(input('Digite o sexo da pessoa:\n[ M ] - Masculino\n[ F ] - Feminino\n')).strip().upper()
if i in 'Mm':
    print('Sua escolha foi Sexo Masculino.')
else:
    print('Sua escolha foi Sexo Feminino.')
print('FIM')