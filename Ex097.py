def esc(msg):
    a = len(msg) + 6
    print('-' * a)
    print(msg, ' '*3)
    print('-' * a)


msg = str(input('Digite sua mensagem:\n'))
esc(msg)
