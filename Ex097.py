def esc(msg):
    a = len(msg)+4
    print('-'*a)
    print(f'  {msg}')
    print('-' * a)


msg = str(input('Digite sua mensagem:\n'))
esc(msg)
