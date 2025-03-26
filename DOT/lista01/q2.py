def area_circulo(r):
    area = 3.14 * r ** r
    return round(area, 2)


def perimetro_circulo(r):
    perimetro = 3.14 * 2 * r
    return round(perimetro, 2)


while True:
    try:
        num = float(input('Digite o valor do raio, em metros: '))
        print(f'O valor da area: {area_circulo(float(num))} m²')
        print(f'O valor do perimetro: {perimetro_circulo(float(num))} m')
        break
    except:
        print('Número inválido. Digite um numero válido para o raio.')
