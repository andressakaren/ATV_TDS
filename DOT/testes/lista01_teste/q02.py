def area_circulo(r):
    area = 3.14 * r ** r
    return round(area, 2)

def perimetro_circulo(r):
    perimetro = 3.14 * 2 * r
    return round(perimetro, 2)

def main():
    assert area_circulo(1) == 3.14
    assert perimetro_circulo(1) == 6.28
    assert area_circulo(2) == round(3.14 * 2 ** 2, 2)  # 2 ** 2 = 4 → 12.56
    assert perimetro_circulo(2.5) == round(3.14 * 2 * 2.5, 2)
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()