"""
Interando strings com for
Função range (start=0, stop, step=1
"""
texto = 'python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)

for n in range(2, 20, 2):
    print(n)
