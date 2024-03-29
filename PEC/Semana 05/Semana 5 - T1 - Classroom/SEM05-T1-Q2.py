def area_e_perimetro(lado):
    area =  lado ** 2 
    perimetro = lado * 4
    return area, perimetro 

lado_quadrado = float(input('Digite o valor do lado do quadrado :'))
area, perimetro = area_e_perimetro(lado_quadrado)
print(f'O valor da área é {area:10.4f}m² e o perímetro do quadrado é {perimetro:10.4f}m')
