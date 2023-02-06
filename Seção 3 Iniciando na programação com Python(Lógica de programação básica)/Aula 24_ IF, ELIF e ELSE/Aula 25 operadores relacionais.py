# Operadores relacionais == igual
# >maior que
# >= maior que ou
# < menor que
# <= menor que ou igual
# != diferente

num_1 = 2
num_2 = 2
expressao = num_1 == num_2

print(expressao)

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)
# limite para pegar empréstimo
idade_limite = 18
if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} Empréstimo negado!')
