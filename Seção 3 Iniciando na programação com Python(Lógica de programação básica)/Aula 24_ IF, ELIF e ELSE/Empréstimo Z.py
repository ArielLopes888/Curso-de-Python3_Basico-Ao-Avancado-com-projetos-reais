deseja = input('Deseja pegar um empréstimo? ')
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
renda = input('qual a sua renda? ')

renda = int(renda)

renda_minima = 1200
variavel_sim = 'SIM'
variavel_nao = 'NÃO'
resposta = str
if renda < renda_minima:
    print(f'{nome},infelizmente seu empréstimo foi negado')
    print('Mas ARIEL BANK, tem outra proposta:')
    resposta = input('Você quer saber? Digite SIM ou NÃO ')

else:
    print(f'{nome}, seu empréstimo foi aprovado! PARABÉNS!!!')

if resposta == 'SIM':
    print(f'Uma outra proposta qualquer')


else:
    print(f"Operação Encerrada!!!")
