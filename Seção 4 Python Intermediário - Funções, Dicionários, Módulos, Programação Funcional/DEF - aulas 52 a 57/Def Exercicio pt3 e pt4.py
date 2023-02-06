"""função 2 que recebe uma função 1 e retorna o valor da função 1 executada"""


def func1():
    return 'Ariel'


def func2(v):
    return v()


nome = func2(func1)
print(nome)

"""função 2 que recebe uma função 1 e retorna o valor da função 1 executada. Função 2 executar duas funções que 
recebam um número diferente de argumentos """


def conssecionária(motos, *args, **kwargs):
    return motos(*args, **kwargs)


def conssecionária2(carros):
    return f'Os {carros} são velozes'


def conssecionária3(bikes, motobikes):
    return f'{bikes} e {motobikes} não são velozes'


comparacao = conssecionária(conssecionária2, 'chevrolet')
comparacao2 = conssecionária(conssecionária3, 'caloi', motobikes='houston')
print(comparacao)
print(comparacao2)
