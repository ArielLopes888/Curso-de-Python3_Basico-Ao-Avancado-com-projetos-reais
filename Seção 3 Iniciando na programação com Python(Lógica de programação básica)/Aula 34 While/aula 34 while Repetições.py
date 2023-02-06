
x = 0
while x < 10:
    if x == 3:
        # break interrompe a contagem e encerra
        # continue interrompe a contagem  no 2 e fica em loop finito
        x = x + 1
        continue  # pula o 3 e continua
    print(x)
    x = x + 1

print('Acabou')
