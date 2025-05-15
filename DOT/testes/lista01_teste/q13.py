def func_S(valor):
    soma = 0 
    for i in range(1, valor + 1):
        soma += 1/i
    return round(soma, 2)

def main():
    assert func_S(1) == 1.0
    assert func_S(2) == round(1 + 1/2, 2)
    assert func_S(5) == round(1 + 1/2 + 1/3 + 1/4 + 1/5, 2)
    assert func_S(10) == round(sum(1/i for i in range(1, 11)), 2)
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
