def max_(a, b, c, d):
    maior = a 
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    if d > maior:
        maior = d
    return maior

def main():
    assert max_(1, 2, 3, 4) == 4
    assert max_(10, 5, 1, 0) == 10
    assert max_(-1, -2, -3, -4) == -1
    assert max_(5, 5, 5, 5) == 5
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
