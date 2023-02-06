# Formatando valores com modificres- Aula 32
""":s - srtrings
:d - int
:f float
:.(numero)f - float
:(caractere)(>esquerda ou <direita ou ^centro ) (quantidade)"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
nome = 'Ariel'
nome_formatado = '{:@>50}'.format(nome)
print(f'{divisao:.2f}')
print(f'{num_1:0<10}')
print(f'{nome:#^50}')
print(nome_formatado)
print(nome.lower())  # tudo minusculo
print(nome.upper())  # tudo maiusculo
print(nome.title())  # primeiras letras maiusculas
