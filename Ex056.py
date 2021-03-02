m = int()
q = int()
ma = int()
mm = int()
me = float()
nma = str()
a = int(input('Digite quantas pessoas tem o Grupo: '))
for c in range(0, a):
    n = str(input('Digite o nome: '))
    i = int(input('Digite a idade: '))
    s = int(input('Digite o sexo:\n[1] para masculino\n[2]para feminino\n'))
    m = m + i
    q = q + 1
    me = float(m / q)
    if s == 1 and i > ma:
        ma = i
        nma = n
    elif s == 2 and i < 20:
        mm = mm + 1
print('A média de idade das pessoas digitas é {:.2f} anos.\nO homem mais velho é o {} com {} anos.\nE no grupo há {} '
      'mulheres com menos de 20 anos.'.format(me, nma, ma, mm))
print('FIM')
