def func_S(valor):
    soma = 0  
    for i in range(1, valor + 1): 
        termo = (i**2 + 1) / (i + 3) 
        soma += termo 
    return round(soma, 2)

def main():
    assert func_S(1) == round((1**2 + 1) / (1 + 3), 2)  # (2/4)
    assert func_S(2) == round((1**2 + 1)/(1+3) + (2**2 + 1)/(2+3), 2)
    assert func_S(3) == round((1**2 + 1)/(1+3) + (2**2 + 1)/(2+3) + (3**2 + 1)/(3+3), 2)
    print("Todos os testes passaram!")

if __name__ == "__main__":
    main()
