frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''
letra_usuario = input('Qual letra deseja deixar maiuscula?')
while contador < tamanho_frase:
    # print(frase[contador], contador)
    # nova_string += frase[contador]
    # print(nova_string)
    # contador += 1

    letra = frase[contador]
    if letra == letra_usuario:
        nova_string += letra_usuario.upper()

    else:
        nova_string += letra
    contador += 1
print(nova_string)
