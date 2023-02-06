nomes = ['riel', 'rielle', 'Osvaldo']

for dados in nomes:
    if dados.lower().startswith('a'):     # lower põe as letras em minusculo, startswith verifica a primeira letra
        print(f'{dados}, = ESSE NOME COMEÇA COM A')

else:
    print('NÃO EXISTEM PALAVRAS QUE COMEÇAM COM "A"')
