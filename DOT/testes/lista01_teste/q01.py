def par_impar(n):
    if n % 2 == 0:
        return True
    return False

def main():
    assert par_impar(2) == True
    assert par_impar(3) == False
    assert par_impar(0) == True
    assert par_impar(-4) == True
    assert par_impar(-3) == False
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
