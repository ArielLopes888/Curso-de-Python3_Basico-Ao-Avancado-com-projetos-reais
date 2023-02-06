horario = input('Diga 0 horário (De 0 - 23): ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Digite um horário apenas entre 0 - 23!!')
    else:
        if horario < 12:
            print('Bom dia!')
        elif horario < 18:
            print('Boa tarde!')

        elif horario <= 23:
            print('Boa noite!')
else:
    ...
