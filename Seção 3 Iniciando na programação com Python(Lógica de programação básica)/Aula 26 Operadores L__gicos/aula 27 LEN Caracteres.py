usuario = input('Digite seu usuário: ')
caracteres = len(usuario)

if caracteres < 6:
    print('Voce precisa digitar pelo menos 6 caracteres')
else:
    print("Voce foi cadastrado no sitema!")

string1 = input('digite alguma coisa: ')
string2 = input('digite outra coisa: ')

print(f'A soma dos caracteres digitados foi: {len(string1) + len(string2)}')
