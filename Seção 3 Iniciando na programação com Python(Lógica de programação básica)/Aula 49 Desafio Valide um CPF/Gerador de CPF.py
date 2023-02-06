# Módulo 1


# Módulo 2

import secrets
  
senha = secrets.token_hex()

  
print(f'Sua senha aleaatória é: {senha}')


# Módulo 3
from random import randint
numero = str(randint(100000000, 999999999))

novo_cpf = numero
reverso = 10
total = 0

for v1 in range(19):
    if v1 > 8:
        v1 = v1 - 9
    total += int(novo_cpf[v1]) * reverso

    reverso = reverso - 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)
        if d > 9:
            d = 0
        novo_cpf += str(d)
        total = 0

print(f'Seu novo CPF é: {novo_cpf}')