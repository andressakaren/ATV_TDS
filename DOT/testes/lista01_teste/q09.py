def soma_intervalo(n1, n2):
    soma = 0
    for i in range(n1, n2 + 1):
        soma += i
    return soma

def main():
    assert soma_intervalo(1, 5) == 15
    assert soma_intervalo(3, 3) == 3
    assert soma_intervalo(-2, 2) == 0
    assert soma_intervalo(0, 0) == 0
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
