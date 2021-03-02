h = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))
imc = p/h**2
if imc < 18.5:
    print('Seu IMC vale {.:2f}, e você é considerado abaixo do peso.'.format(imc))
elif imc < 25:
    print('Seu IMC vale {:.2f}, e vovê é considero com peso ideal.'.format(imc))
elif imc < 30:
    print('Seu IMC vale {:.2f}, e você é considerado com sobre peso.'.format(imc))
elif imc < 40:
    print('Seu IMC vale {:.2f}, e você é considerado com obesidade.'.format(imc))
elif imc >= 40:
    print('Seu IMC vale {:.2f}, e você é considerado com obesidade mórbida.'.format(imc))
print('\nFIM')