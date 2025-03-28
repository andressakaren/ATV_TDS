def par_impar(n):
    if n % 2 == 0:
        return True
    return False

while True:
    try:
        num = int(input('Digite um numero: '))
        if par_impar(num) == True:
            print(f'O numero {num} é par.')
        else:
            print(f'O numero {num} é ímpar.')
        break
    except:
        print('Número inválido. Digite um numero válido.')

        