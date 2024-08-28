def main():
    # a) preencha com 0 (zero) e imprima a lista; 
    n = int(input())
    lista = [0] * n
    print(lista)
    
    # b) preencha com os números de 1 a n e imprima a lista; 
    lista = list(range(1, n + 1))
    print(lista)
    
    # ACHO Q TEM NOVO INPUT dentro do FOR ??????? 
    # Usar o n para definir a quantidade de valores a ser lido depois pelo teclado 
    # c) preencha com valores lidos pelo teclado e imprima a lista; 
    lista = []
    for i in range(n):
        lista.append(int(input()))
    print(lista)
    
    # d) preencha na ordem inversa com valores lidos pelo teclado e imprima a lista; dica: use insert para sempre incluir os elementos no início da lista;   
    lista = []
    for i in range(n):
        lista.insert(0, int(input()))
    print(lista)
       
if __name__ == "__main__":
    main()