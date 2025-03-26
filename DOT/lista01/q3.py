def fahrenheit_para_celsius(valor):
    c = ((valor - 32) / 9) * 5
    return round(c, 2)


while True:
    try:
        valor = float(input('Digite o valor da temperatura em Fahrenheit: '))
        print(
            f'Fahrenheit: {valor:.2f}°F \nCelsius: {fahrenheit_para_celsius(valor)}°C')
        break
    except:
        print('Valor inválido. Digite um numero válido.')
