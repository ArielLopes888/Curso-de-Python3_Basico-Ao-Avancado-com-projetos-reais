nome = input('Digite o seu primeiro nome: ')
letras = len(nome)

if letras < 5:
    print("Seu nome é curto")
elif letras == 5 or letras == 6:
    print("Seu nome é normal")
else:
    print('Seu nome é muito grande')

