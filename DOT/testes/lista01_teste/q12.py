def somatorio(valor):
    count = 0
    for i in range(1, valor + 1):
        count += i
    return count

def main():
    assert somatorio(1) == 1
    assert somatorio(5) == 15
    assert somatorio(10) == 55
    assert somatorio(0) == 0
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
