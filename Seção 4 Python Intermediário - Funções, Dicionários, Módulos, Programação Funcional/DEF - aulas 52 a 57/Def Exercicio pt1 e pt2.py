""" função que exibe parâmetros saudação e nome"""


def apresent(sdd='Olá', msg='Ariel'):
    print(sdd, msg)


apresent()

"""Função que recebe 3 números e exiba a soma entre eles"""


def soma(n1, n2, n3):
    return n1 + n2 + n3


somar = soma(5, 4, 5)
print(somar)

"""Funçao que receba 2 numeros. Retornar a soma do primeiro valor mais 10% """


def aumento_centual(number, percentual):
    return number + (number * percentual / 100)


porcent = aumento_centual(10, 20)
print(f' Este é o resultado da porcentagem: {porcent}')

"""FIZZ BUZZ"""


def fizzbuzz(numbers=input('Digite um número: ')):
    numbers = int(numbers)
    if numbers % 3 == 0 and numbers % 5 == 0:
        return "fizzbuzz"
    if numbers % 3 == 0:
        return "fizz"
    if numbers % 5 == 0:
        return "buzz"
    return numbers


print(fizzbuzz())
