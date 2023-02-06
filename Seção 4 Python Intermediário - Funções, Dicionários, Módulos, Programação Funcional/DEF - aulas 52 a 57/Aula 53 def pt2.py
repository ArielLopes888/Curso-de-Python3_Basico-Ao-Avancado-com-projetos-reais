def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


divide = divisao(8, 2)
if divide:
    print(divide)
else:
    print('Conta Inválida')


def dumb():
    return 'Luiz', 'Otávio'    # tuplas são listas que não podem ser alteradas


var = dumb()
print(var, type(var))
