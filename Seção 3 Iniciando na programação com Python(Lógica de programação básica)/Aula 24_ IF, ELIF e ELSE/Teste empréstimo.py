nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade?')
idade = int(idade)

# Limite para pegar empréstmo
idade_menor = 20
idade_maior = 30

if idade_menor <= idade <= idade_maior:
    print(f'{nome}! Empréstimo Aprovado!!!')
else:
    print(f'{nome}, Infelizmente o empréstimo foi negado!')
