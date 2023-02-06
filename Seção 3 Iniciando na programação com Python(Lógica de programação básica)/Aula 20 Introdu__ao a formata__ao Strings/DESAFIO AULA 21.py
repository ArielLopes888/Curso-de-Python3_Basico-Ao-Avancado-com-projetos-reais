nome = 'Ariel'
idade = 25
altura = 1.80
peso = 84
ano_atual = 2022
data_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print('{n} tem {i} anos, {a} de altura e pesa {p}kg'.format(n=nome, i=idade, a=altura, p=peso))
print('{0} tem {1} anos, {2} de altura e pesa {3}kg'.format(nome, idade, altura, peso))  # sempre começar por zero0
print('O IMC de {} é {:.2f}'.format(nome, imc))
print('{0} nasceu em {1}'.format(nome, data_nascimento))
print(' ')
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f} ')
print(f'{nome} nasceu em {data_nascimento}')
