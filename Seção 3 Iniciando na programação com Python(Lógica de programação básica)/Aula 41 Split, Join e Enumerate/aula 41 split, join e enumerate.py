"""Split - dividir uma str  gerando listas       ## .split remover do inicio e fim da string ### .capitalize deixar
primeira letra maiuscula Join - Juntar uma lista Enumarate - Enumerar elementos da lista # iteráveis """

string = 'O Brasil é o país do futebol, o Brasil é penta.'
lista1 = string.split(' ')
lista2 = string.split(',')
print(lista1)
print(lista2)

palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'  A palavra que apareceu mais vezes é {palavra}! ({contagem}x). ')

join = '#'.join(lista1)
print(join)

for indice, v2 in enumerate(lista1):
    print(indice, v2)
