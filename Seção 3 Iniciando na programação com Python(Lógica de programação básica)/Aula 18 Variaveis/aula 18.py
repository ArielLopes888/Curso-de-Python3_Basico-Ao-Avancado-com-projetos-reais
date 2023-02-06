"""
variaveis iniciam com letra, mas pode conter números, separar com _, letras minusculas 
"""''
nome = 'Ariel'
idade = 25
altura = 1.80
e_maior = idade > 18
peso = 84
imc = peso / (altura ** 2)
print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)
print('Peso:', peso)
print(idade * altura)

print(nome, 'tem', idade, 'anos de idade e seu imc é:', imc, '!')
