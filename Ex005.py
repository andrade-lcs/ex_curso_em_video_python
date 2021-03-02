
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
sb = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
dr = n1%n2
p = n1**n2
po = pow(n1,n2)
print('A soma é {:-^5}.\n Subtração é {:-^5}.\n A multiplicação é {:-^5}.\n A Divisão é {:-^5.3f} '.format(s, sb, m, d))
print('A divisão interia é {:-^5}.\n O resto da divisão é{:-^5}.\n A potência é {:-^5}.\n A potência é {:-^5}'.format(di, dr, p, po))