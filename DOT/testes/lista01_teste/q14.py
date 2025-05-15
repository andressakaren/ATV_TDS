def func_S(valor):
    soma = 1  
    fatorial = 1 
    
    for i in range(1, valor + 1): 
        fatorial *= i 
        soma += 1 / fatorial 

    return round(soma, 2)

def main():
    assert func_S(1) == round(1 + 1/1, 2)
    assert func_S(2) == round(1 + 1/1 + 1/2, 2)
    assert func_S(3) == round(1 + 1/1 + 1/2 + 1/6, 2)
    assert func_S(5) == round(sum(1 / math.factorial(i) for i in range(0, 6)), 2)
    print("Todos os testes passaram!")

if __name__ == "__main__":
    import math
    main()
