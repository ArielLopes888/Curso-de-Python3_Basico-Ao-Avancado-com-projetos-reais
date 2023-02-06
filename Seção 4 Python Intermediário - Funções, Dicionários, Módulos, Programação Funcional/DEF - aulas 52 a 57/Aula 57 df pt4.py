variavel = 'valor'  # escopo global


def func():
    print(variavel)


def func2():
    # global variavel (altero o valor da variavel em escopo global) não é uma boa prática
    variavel = 'Outro valor'     # escopo local
    print(variavel)


func()
func2()

print(variavel)
