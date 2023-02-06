nome = input("Qual o seu nome? ")
altura = float(input('Qual a sua altura? '))
peso = int(input('Qual o seu peso? '))
imc = (peso / altura ** 2)

print(f'O usuário se chama {nome}, e seu IMC é: {imc:.2f}!')
