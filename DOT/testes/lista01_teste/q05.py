def peso_ideal(altura, sexo):
    if sexo == 1:
        return round((62.1 * altura) - 44.7, 2)
    if sexo == 2:
        return round((72.7 * altura) - 58, 2)

def main():
    assert peso_ideal(1.70, 1) == round((62.1 * 1.70) - 44.7, 2)
    assert peso_ideal(1.70, 2) == round((72.7 * 1.70) - 58, 2)
    assert peso_ideal(1.50, 1) == round((62.1 * 1.50) - 44.7, 2)
    print("Todos os testes da QUESTÃO 5 passaram!")

if __name__ == "__main__":
    main()
