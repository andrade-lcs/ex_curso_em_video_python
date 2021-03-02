from Teste.Lib.interface import *
from Teste.Lib.arquivo import *
from Teste.Lib.DBPs import *
from time import sleep

arq = 'Bacia_Def.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver Bacias Cadastradas', 'Cadastrar Nova Bacia', 'Calculo de Parâmetros', 'Sair do Sistema'])
    if resposta == 1:
        lerarquivo(arq)
        continuar(resposta)
    elif resposta == 2:
        cabeçalho('Novo Cadastro')
        while True:
            d0 = leiaint('D0: ')
            if d0 == 000:
                break
            d20 = leiaint('D20: ')
            d30 = leiaint('D30: ')
            d45 = leiaint('D45: ')
            d60 = leiaint('D60: ')
            d90 = leiaint('D90: ')
            d120 = leiaint('D120: ')
            cadastrar(arq, d0, d20, d30, d45, d60, d90, d120)
            sci = d0 - d30
            bci = d30 - d60
            bdi = d60 - d90
            d25 = (d20+d30)/2 #calcular D25 por agnesis
            rc = 6250/(2*(d0-d25))
            area = 10*(1+1.5*d20/d0+1.25*d30/d0+1.5*d45/d0+2.25*d60/d0+1.5*d90/d0)
            cadastrardbps(arqc, d0, rc, area, sci, bci, bdi)
            break
    elif resposta == 3:
        menudbps(arqc)
    if resposta == 4:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('\033[31mERRO! digite uma opção válido.\033[m')
    sleep(2)
cabeçalho('FIM')