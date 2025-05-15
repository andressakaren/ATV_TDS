def fahrenheit_para_celsius(valor):
    c = ((valor - 32) / 9) * 5
    return round(c, 2)

def main():
    assert fahrenheit_para_celsius(32) == 0.0
    assert fahrenheit_para_celsius(212) == 100.0
    assert fahrenheit_para_celsius(98.6) == 37.0
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
