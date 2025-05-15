def num_ao_cubo(valor):
    return valor ** 3

def main():
    assert num_ao_cubo(2) == 8
    assert num_ao_cubo(-3) == -27
    assert num_ao_cubo(0) == 0
    assert num_ao_cubo(1.5) == 3.375
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
