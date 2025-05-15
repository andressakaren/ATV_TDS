def numeroDivisores(valor):
    count = 0
    for i in range(1, valor + 1):
        if valor % i == 0:
            count += 1
    return count

def main():
    assert numeroDivisores(1) == 1
    assert numeroDivisores(6) == 4   # 1, 2, 3, 6
    assert numeroDivisores(10) == 4  # 1, 2, 5, 10
    assert numeroDivisores(13) == 2  # primo
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
