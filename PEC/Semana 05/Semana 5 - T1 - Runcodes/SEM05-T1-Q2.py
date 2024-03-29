def area_e_perimetro(lado):
    area =  lado ** 2 
    perimetro = lado * 4
    return area, perimetro 

lado_quadrado = float(input(''))
area, perimetro = area_e_perimetro(lado_quadrado)
print(f'{area:10.4f}')
print(f'{perimetro:10.4f}')
