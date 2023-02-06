"""*args **kwargs"""


# **kwargs argumentos nomeados

def func(*args):  # pode-se usar quando não sei quantos argumentos virá na def / empacotamento e desempacotamento
    print(args)


lista = [1, 2, 3, 4, 5]
print(*lista, sep='%')
