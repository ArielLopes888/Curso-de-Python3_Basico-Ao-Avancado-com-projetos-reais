nome = 'Ariel'
idade = 25
altura = 1.80
e_maior = idade > 18
peso = 84
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é:', imc, '!')
print(f'{nome} tem {idade} anos de idade e seu imc é {imc} !')
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f} !')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos e seu imc é {2:.2f} {0}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
