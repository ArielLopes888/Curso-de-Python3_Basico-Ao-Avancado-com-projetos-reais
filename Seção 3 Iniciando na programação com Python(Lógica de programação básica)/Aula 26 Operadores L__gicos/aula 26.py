"""
Operadores Lógicos: and, or, not, in, not in
"""

# USO DO AND verdadeiro e verdadeiro = true

Ariel = 25
Arielle = 20

if Ariel and Arielle >= 26:
    print('Correto')
else:
    print('Errado')

# USO DO OR verdadeiro ou verdadeiro = true
if Ariel or Arielle == 25:
    print('Correto')
else:
    print('Errado')

# USO DO NOT #conhecido como inversor
if not Ariel or Arielle == 25:
    print('Correto')
else:
    print('Incorreto')

a = ''
b = 0
if not b:
    print("Por favor preencha login e senha")
else:
    print('Dados Corretos')

# USO DO IN
nome = 'Ariel'
if 'l' in nome:
    print('Existe a letra L no seu nome')

# USO DO NOT IN
if 'u' not in nome:
    print('Não tem U no seu nome')
