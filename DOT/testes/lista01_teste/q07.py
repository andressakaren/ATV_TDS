def calc_fatorial(n):
    mult_fatorial = 1
    for i in range(1, n + 1):
        mult_fatorial *= i 
    return mult_fatorial

def main():
    assert calc_fatorial(0) == 1
    assert calc_fatorial(1) == 1
    assert calc_fatorial(5) == 120
    assert calc_fatorial(7) == 5040
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
