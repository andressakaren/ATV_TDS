def calc_perimetro(l):
    return round(l * 3, 2)
    
def calc_area(l):
    return round(l ** 2, 2)

def main():
    assert calc_perimetro(3) == 9.00
    assert calc_perimetro(5.5) == 16.5
    assert calc_area(2) == 4.00
    assert calc_area(3.3) == round(3.3 ** 2, 2)
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
