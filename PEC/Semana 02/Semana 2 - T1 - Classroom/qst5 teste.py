while True:
    try:
        nivel = int(input('''Qual seu nível de empolgação, de 1 a 5? 
Sendo: 
1 - pouco empolgado.
5 - muito empolgado. 
'''))
        if not 1 <= nivel <= 5:
            raise ValueError('Valor fora do intervalo permitido')
        break
    except ValueError as error:
        print(error)

if 1 <= nivel <= 5:
    print(f'Sua empolgação é nível {nivel} >>> G{nivel * 'o'}L!')
