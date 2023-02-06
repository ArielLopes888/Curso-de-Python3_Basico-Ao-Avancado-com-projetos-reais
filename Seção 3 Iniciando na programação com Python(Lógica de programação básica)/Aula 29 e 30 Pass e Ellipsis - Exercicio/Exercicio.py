numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero = int(numero)
    resto = numero % 2

    if resto == 0:
        print('Esse numero é par!')
    else:
        print('Esse numero é ímpar!')
else:
    print('Digite apenas números inteiros')
