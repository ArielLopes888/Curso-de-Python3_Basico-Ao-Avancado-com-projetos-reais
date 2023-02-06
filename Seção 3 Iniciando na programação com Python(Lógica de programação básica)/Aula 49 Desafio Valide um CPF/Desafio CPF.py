cpf = input('Digite seu CPF: ')
cpf_verifador = cpf[:-2]
reverso = 10
total = 0

for v1 in range(19):
    if v1 > 8:
        v1 = v1 - 9
    total += int(cpf_verifador[v1]) * reverso

    reverso = reverso - 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)
        if d > 9:
            d = 0
        cpf_verifador += str(d)
        total = 0

if cpf_verifador == cpf:
    print('CPF Válido')
else:
    print('CPF Invalido')
