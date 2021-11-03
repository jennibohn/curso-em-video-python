peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso/(altura**2)
print('O valor do IMC é {}'.format(imc))
if(imc < 18.5):
    print('Magreza')
elif(imc < 24.9):
    print('Normal')
elif(imc < 29.9):
    print('Sobrepeso')
elif(imc<39.9):
    print('Obesidade I')
else:
    print('Obesidade II')